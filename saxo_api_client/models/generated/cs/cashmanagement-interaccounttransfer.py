"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class InteraccounttransferRequest(_FlexModel):
    Amount: Optional[float] = Field(default=None, alias="Amount", description="The amount")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="The currency")
    FromAccountKey: Optional[Any] = Field(default=None, alias="FromAccountKey", description="Source account")
    ToAccountKey: Optional[Any] = Field(default=None, alias="ToAccountKey", description="Destination account")
    WithdrawalReasonId: Optional[int] = Field(default=None, alias="WithdrawalReasonId", description="Withdrawal Reason Id")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
