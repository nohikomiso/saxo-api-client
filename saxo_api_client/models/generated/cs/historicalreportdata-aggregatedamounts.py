"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetallaggregatedamountsbetweentwodatesRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    skiptoken: Optional[str] = Field(default=None, alias="$skiptoken", description="Specifies an entity id to start retrieving entries from. This is normally only used in generated nextlinks.")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the resource belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The key of the account to which the resource belongs.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the resource belongs.")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="From date")
    MockDataId: Optional[str] = Field(default=None, alias="MockDataId", description="Optional Mock Data Parameter")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="To date")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
