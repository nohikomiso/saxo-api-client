"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class FetchesasummaryoftransfersRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="If specified, will only return entries pertaining to the specified account.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="If specified, will only return entries pertaining to the specified client.")
    ExternalReference: Optional[str] = Field(default=None, alias="ExternalReference", description="Include entries with the specified ExternalReference.")
    FromDateTime: Optional[str] = Field(default=None, alias="FromDateTime", description="Only include entries with a TransferRequestedOn value greater than or equal to FromDateTime.")
    SkipToken: Optional[str] = Field(default=None, alias="SkipToken", description="Id token of entity to start taking elements from.")
    ToDateTime: Optional[str] = Field(default=None, alias="ToDateTime", description="Only include entries with a TransferRequestedOn value lower than or equal to ToDateTime.")
    Top: Optional[int] = Field(default=None, alias="Top", description="Number of elements to retrieve. (Default is 50, Max is 1000.)")

class FundingCheck(_FlexModel):
    Enforce: Optional[Any] = Field(default=None, alias="Enforce", description="")
    Ignore: Optional[Any] = Field(default=None, alias="Ignore", description="")

class CashtransferinitiatedbypartnerRequest(_FlexModel):
    Amount: Optional[float] = Field(default=None, alias="Amount", description="The value that will be transacted.")
    Comment: Optional[str] = Field(default=None, alias="Comment", description="Comment to the transaction. The comment will be seen in the EOD files.")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency in which the cash movement will be held in. This is essentially just an extra check! The currency entered here must be the same as that of the funding account and the clients trading account.")
    ExternalReference: Optional[str] = Field(default=None, alias="ExternalReference", description="Caller may add this to identify the request.")
    FromAccountKey: Optional[Any] = Field(default=None, alias="FromAccountKey", description="Account from where the cash is moved from. For funding transactions, this field will hold the AccountKey of the funding account. For withdrawal transactions this field will hold the AccountKey of the clients trading account. Remember that the currency of the funding account and the clients trading account must be the same.")
    FundingCheck: Optional[FundingCheck] = Field(default=None, alias="FundingCheck", description="Specify this to specify if funding rules be checked and enforced. Default is 'Enforce'. Enforce: All margin and funding checks will be performed and enforced.The transaction will fail if margin and funding checks are not passed. Ignore: No margin or funding checks are performed.The operation will move the specified monies from the client account and you can ultimately place the clients accounts into negative. You can only specify FundingCheck:Ignore for a cash withdrawal from a clients trading account back to the WLC's funding account. If you specify FundingCheck:Ignore for a funding from the WLC's funding account to the clients trading account, the call will fail.")
    ToAccountKey: Optional[Any] = Field(default=None, alias="ToAccountKey", description="Account where the cash is moved to. For funding transactions, this field will hold the AccountKey of the clients trading account. For withdrawal transactions this field will hold the AccountKey of the WLCs funding account. Remember that the currency of the funding account and the clients trading account must be the same.")
    ValueDate: Optional[Any] = Field(default=None, alias="ValueDate", description="Value Date of settlement of cash transfer. Must be within the range [-90;90] days of current date.")

class FetchesthelateststatusoffundtransfersRequest(_FlexModel):
    TransactionId: Optional[str] = Field(default=None, alias="TransactionId", description="")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
