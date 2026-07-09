"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class BookingRequestType(_FlexModel):
    BkAmountId: Optional[Any] = Field(default=None, alias="BkAmountId", description="Booking amount Id")
    BkAmountTypeId: Optional[Any] = Field(default=None, alias="BkAmountTypeId", description="SaxoInternal- Booking Amount type Id")
    CaMasterRecordId: Optional[Any] = Field(default=None, alias="CaMasterRecordId", description="Corporate action Id")
    RelatedTradeId: Optional[Any] = Field(default=None, alias="RelatedTradeId", description="Related trade Id")

class GetallbookingsforClientKeybetweentwodatesorbyspecifyingacombinationofFilterTypeandFilterValueRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    skiptoken: Optional[str] = Field(default=None, alias="$skiptoken", description="Specifies an entity id to start retrieving entries from. This is normally only used in generated nextlinks.")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the resource belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The key of the account to which the resource belongs.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the resource belongs.")
    FilterType: Optional[BookingRequestType] = Field(default=None, alias="FilterType", description="Type, basis on which bookings are reterived. If specified you must also specify a FilterValue")
    FilterValue: Optional[str] = Field(default=None, alias="FilterValue", description="Id for the specified filter type.")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="From date, ignored when filterType and filterValue are not null")
    MockDataId: Optional[str] = Field(default=None, alias="MockDataId", description="Optional Mock Data Parameter")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="To date, ignored when filterType and filterValue are not null")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
