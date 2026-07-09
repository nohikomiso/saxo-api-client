"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class RequestapasswordresetRequest(_FlexModel):
    Email: Optional[str] = Field(default=None, alias="Email", description="E-mail address of the user")
    Language: Optional[str] = Field(default=None, alias="Language", description="Service language code - Default is English")
    UserId: Optional[Any] = Field(default=None, alias="UserId", description="User's client ID")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
