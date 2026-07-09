"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class SortColumn(_FlexModel):
    AccountId: Optional[Any] = Field(default=None, alias="AccountId", description="Account id")
    Cins: Optional[Any] = Field(default=None, alias="Cins", description="Cins")
    Cusip: Optional[Any] = Field(default=None, alias="Cusip", description="Cusip")
    CutoffDate: Optional[Any] = Field(default=None, alias="CutoffDate", description="Cutoff date")
    DeliveryType: Optional[Any] = Field(default=None, alias="DeliveryType", description="DeliveryType")
    DeliveryTypeDescription: Optional[Any] = Field(default=None, alias="DeliveryTypeDescription", description="Delivery type description")
    Isin: Optional[Any] = Field(default=None, alias="Isin", description="Isin")
    IssuerName: Optional[Any] = Field(default=None, alias="IssuerName", description="Issuer name")
    JobNumber: Optional[Any] = Field(default=None, alias="JobNumber", description="Job number")
    RecievedDate: Optional[Any] = Field(default=None, alias="RecievedDate", description="Recieved date")
    Status: Optional[Any] = Field(default=None, alias="Status", description="Status")
    StatusDate: Optional[Any] = Field(default=None, alias="StatusDate", description="Status date")
    SubType: Optional[Any] = Field(default=None, alias="SubType", description="Sub type")
    SubTypeDescription: Optional[Any] = Field(default=None, alias="SubTypeDescription", description="Sub type description")
    Ticker: Optional[Any] = Field(default=None, alias="Ticker", description="Ticker")
    Type: Optional[Any] = Field(default=None, alias="Type", description="Type")
    TypeDescription: Optional[Any] = Field(default=None, alias="TypeDescription", description="Type description")

class SortType(_FlexModel):
    Asc: Optional[Any] = Field(default=None, alias="Asc", description="Ascending sort")
    Desc: Optional[Any] = Field(default=None, alias="Desc", description="Descending sort")

class GetproxyeventsRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Unique identifier of an Account.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique identifier of a Client.")
    SortColumn: Optional[SortColumn] = Field(default=None, alias="SortColumn", description="Specify a column to sort on. Default sorting on records is descending by ReceivedDate and ascending by IssuerName.")
    SortType: Optional[SortType] = Field(default=None, alias="SortType", description="Specify ascending or descending sort. Default sort type will be Ascending.")

class RetrievesthefeesforaproxyvotingeventRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Unique identifier of an account.")
    JobNumber: Optional[str] = Field(default=None, alias="JobNumber", description="6-character Broadridge generated internal identifier used to track the event.")

class AcceptproxyfeeRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Unique identifier of an Account.")
    FeeDisclaimerKey: Optional[str] = Field(default=None, alias="FeeDisclaimerKey", description="The key provided when rendering possible fees that may be incurred by the client due to this voting action.")
    JobNumber: Optional[str] = Field(default=None, alias="JobNumber", description="6-character identifier for proxy event.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
