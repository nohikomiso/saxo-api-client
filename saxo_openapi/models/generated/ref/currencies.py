"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class CurrencyDetails(_FlexModel):
    CurrencyCode: Optional[str] = Field(default=None, alias="CurrencyCode", description="The currency's ISO 3166-1 code.")
    Decimals: Optional[int] = Field(default=None, alias="Decimals", description="Number of decimals used in minor currency.")
    Name: Optional[str] = Field(default=None, alias="Name", description="Name of the currency.")
    Symbol: Optional[str] = Field(default=None, alias="Symbol", description="Symbol of the currency.")

class GetallsupportedcurrenciesRequest(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[CurrencyDetails]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
