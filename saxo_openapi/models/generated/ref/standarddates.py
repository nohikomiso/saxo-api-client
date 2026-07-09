"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class GetalistofforwardtenordatesRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Account to which short tenor permissions are checked against. Short tenors are not returned if no account is specified.")
    Uic: Optional[Any] = Field(default=None, alias="Uic", description="The Universal Instrument Code (UIC) of the instrument to get.")

class GetalistofFXoptionexpirydatesRequest(_FlexModel):
    Uic: Optional[Any] = Field(default=None, alias="Uic", description="The Universal Instrument Code (UIC) of the instrument to get.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
