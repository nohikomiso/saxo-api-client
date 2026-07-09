"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class SearchCriteriaFieldGroups(_FlexModel):
    Accounts: Optional[Any] = Field(default=None, alias="Accounts", description="Accounts field in the response will only be displayed if field group is Accounts.")
    Default: Optional[Any] = Field(default=None, alias="Default", description="The default value. The search response will not contain Accounts info if nothing is provided in the FieldGroups field.")
    Users: Optional[Any] = Field(default=None, alias="Users", description="Users field in the response will only be displayed if FiledGroups list contains Users.")

class SearchallchildcounterpartsbasedonownerIdRequest(_FlexModel):
    inlinecount: Optional[str] = Field(default=None, alias="$inlinecount", description="Specifies that the response to the request should include a count of the number of entries in the collection")
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountId: Optional[str] = Field(default=None, alias="AccountId", description="AccountId to search")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="AccountKey to search")
    ClientId: Optional[str] = Field(default=None, alias="ClientId", description="ClientId to search")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="ClientKey to search")
    FieldGroups: Optional[List[SearchCriteriaFieldGroups]] = Field(default=None, alias="FieldGroups", description="FieldGroups controlling the presence of different fields in the response")
    Keywords: Optional[str] = Field(default=None, alias="Keywords", description="Text to search in other fields, must be at least 3 characters (with at least one letter) - otherwise 4+ digits is needed")
    UserId: Optional[str] = Field(default=None, alias="UserId", description="UserId to search")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
