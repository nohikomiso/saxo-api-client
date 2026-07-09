"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class CountryDetails(_FlexModel):
    A3: Optional[str] = Field(default=None, alias="A3", description="3-letter ISO-3166 country code.")
    CountryCode: Optional[str] = Field(default=None, alias="CountryCode", description="2-letter ISO-3166 country code. (Also called A2 in ISO 3166 standard).")
    DisplayName: Optional[str] = Field(default=None, alias="DisplayName", description="Name of the country in the language selected by the user.")
    Name: Optional[str] = Field(default=None, alias="Name", description="Name of the country in English.")
    Numeric: Optional[int] = Field(default=None, alias="Numeric", description="Numeric country code.")

class GetallsupportedcountriesRequest(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[CountryDetails]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
