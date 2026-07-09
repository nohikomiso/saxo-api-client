"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class CreateaccountRequest(_FlexModel):
    ChoiceOfAccount: Optional[str] = Field(default=None, alias="ChoiceOfAccount", description="Choice Of Account (from Options)")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Client Key of the user for which new account is to be created")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
