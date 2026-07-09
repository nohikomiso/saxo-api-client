"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetwiretransferinstructionsforspecifiedclientandaccountRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Selected account key in which user will fund.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Logged-in client key")
    CurrencyCode: Optional[str] = Field(default=None, alias="CurrencyCode", description="Transaction currency.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
