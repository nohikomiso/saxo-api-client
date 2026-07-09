"""Utility classes and/or functions."""

import saxo_api_client.endpoints.referencedata as rd
from saxo_api_client.definitions.orders import AssetType


def InstrumentToUic(client, AccountKey, spec, assettype=AssetType.FxSpot):
    """replace the Instrument for a Uic in the spec dict.
    If there is no Instrument in spec the spec gets returned untouched.

    In case there are multiple entries returned and ValueError is raised.

    Parameters
    ----------

    client : API client instance (required)
        the API client instance

    AccountKey : string (required)
        the AccountKey of the account

    spec : dict (required)
        the dictionary to process. If it contains an 'Instrument' key, try
        to replace it by a Uic

    assettype : string (required: default 'FxSpot')
        the assettype used in the query with the Instrument

    Example
    -------

    >>> from saxo_api_client import API
    >>> from saxo_api_client.contrib.util import InstrumentToUic
    >>> from pprint import pprint
    >>> token = "..."
    >>> AccountKey = "..."
    >>> client = API(access_token=token)
    >>> spec = {'Instrument': 'EURUSD', 'Amount': 120000}
    >>> # find the Uic for Instrument
    >>> pprint(InstrumentToUic(client, AccountKey, spec=spec))
    {'Amount': 120000, 'Uic': 21}
    """

    if "Instrument" in spec:
        params = {
            "AccountKey": AccountKey,
            "AssetTypes": assettype,
            "Keywords": spec.get("Instrument"),
        }

        # create the request to fetch Instrument info
        r = rd.instruments.Instruments(params=params)
        rv = client.request(r)
        
        data = rv.get("Data", [])
        if not data:
            raise ValueError("No instruments found for: {}".format(spec["Instrument"]))
            
        uic = None
        if len(data) == 1:
            uic = data[0]["Identifier"]
        else:
            # 複数ヒットした場合の賢い絞り込みロジック
            # 1. Identifier が PrimaryListing と一致しているもの（本家）を優先
            primary_matches = [item for item in data if item.get("Identifier") == item.get("PrimaryListing")]
            
            if len(primary_matches) == 1:
                uic = primary_matches[0]["Identifier"]
            elif len(primary_matches) > 1:
                # それでも複数ある場合は、ExchangeIdが指定されていればそれを使う、等も考えられるが
                # まずは先頭を採用してログを出すか、最初に見つかったものを返す
                uic = primary_matches[0]["Identifier"]
            else:
                # PrimaryListing が一致するものがない場合（珍しいケース）は先頭を返す
                uic = data[0]["Identifier"]

        if uic is not None:
            del spec["Instrument"]
            spec.update({"Uic": uic})
        else:
            raise ValueError("Could not resolve Uic for: {}".format(spec["Instrument"]))

    return spec
