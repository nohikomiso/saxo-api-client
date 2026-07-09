"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class OrderEntryType(_FlexModel):
    All: Optional[Any] = Field(default=None, alias="All", description="EntryType:- All: Return all entries pertaining to any order.")
    Last: Optional[Any] = Field(default=None, alias="Last", description="EntryType:- Last: Only return the latest state of an order.")

class OrderActivityFieldGroup(_FlexModel):
    DisplayAndFormat: Optional[Any] = Field(default=None, alias="DisplayAndFormat", description="Display and Format.")

class OrderLogStatus(_FlexModel):
    Cancelled: Optional[Any] = Field(default=None, alias="Cancelled", description="Order cancel initiated by client or dealer.")
    Changed: Optional[Any] = Field(default=None, alias="Changed", description="Order change.")
    DoneForDay: Optional[Any] = Field(default=None, alias="DoneForDay", description="Order is done for day in external OMS.")
    Expired: Optional[Any] = Field(default=None, alias="Expired", description="Order has expired.")
    Fill: Optional[Any] = Field(default=None, alias="Fill", description="Order fill - (Also used for trade on quote in OrderLog)")
    FinalFill: Optional[Any] = Field(default=None, alias="FinalFill", description="Order fill - final fill of an open order.")
    Placed: Optional[Any] = Field(default=None, alias="Placed", description="New order placement.")
    Working: Optional[Any] = Field(default=None, alias="Working", description="System or dealer initiated order placement in external OMS of existing order.")

class QueryOrderactivitieshistoryRequest(_FlexModel):
    skiptoken: Optional[str] = Field(default=None, alias="$skiptoken", description="Specifies an entity id to start retrieving entries from. This is normally only used in generated nextlinks.")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Account key: If specified will only return entries pertaining to specified Account.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Client key: If specified will only return entries pertaining to specified client and its sub clients depending upon includeSubAccounts.")
    CorrelationKey: Optional[str] = Field(default=None, alias="CorrelationKey", description="CorrelationKey: If specified, will only return entries with the specified CorrelationKey")
    EntryType: Optional[OrderEntryType] = Field(default=None, alias="EntryType", description="EntryType: optional. Defaults to 'All': Return all entries pertaining to any order. 'Last': Only return the latest state of an order ignoring ToDateTime (if any).")
    FieldGroups: Optional[List[OrderActivityFieldGroup]] = Field(default=None, alias="FieldGroups", description="FieldGroups: DisplayAndFormat")
    FromDateTime: Optional[Any] = Field(default=None, alias="FromDateTime", description="Only include entries, with a ActivityDateTime greater than or equal to FromDateTime")
    IncludeSubAccounts: Optional[bool] = Field(default=None, alias="IncludeSubAccounts", description="IncludeSubAccounts: If specified true will return entries for all clients under specified ClientId in a hierarchy.")
    OrderId: Optional[str] = Field(default=None, alias="OrderId", description="OrderId: Will only return entries pertaining to specified OrderId")
    Status: Optional[List[OrderLogStatus]] = Field(default=None, alias="Status", description="Status: If specified will only return entries with the specified OrderStatus")
    ToDateTime: Optional[Any] = Field(default=None, alias="ToDateTime", description="Only include entries, with a ActivityDateTime less than or equal to ToDateTime. Cannot be used with EntryType='Last'")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
