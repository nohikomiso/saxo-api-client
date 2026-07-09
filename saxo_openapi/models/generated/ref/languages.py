"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class LanguageDetails(_FlexModel):
    LanguageCode: Optional[Any] = Field(default=None, alias="LanguageCode", description="The ISO 639-1 two-letter language code. (Except for zh-cn and zh-tw). This list only includes languages for which Saxo has full or partial support for translation of texts.")
    LanguageName: Optional[str] = Field(default=None, alias="LanguageName", description="The name of the language (in English).")
    NativeName: Optional[str] = Field(default=None, alias="NativeName", description="The name of the language (in native language).")

class GetallsupportedlanguagesRequest(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[LanguageDetails]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
