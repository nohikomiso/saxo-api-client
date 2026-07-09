"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class OptionInstruction(_FlexModel):
    Amount: Optional[float] = Field(default=None, alias="Amount", description="Quantity to be elected")
    OptionId: Optional[str] = Field(default=None, alias="OptionId", description="Option on which election is to be made")
    Remarks: Optional[str] = Field(default=None, alias="Remarks", description="Remarks by client")

class SendelectioninstructionRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Account on which elections are to be made")
    EventId: Optional[str] = Field(default=None, alias="EventId", description="Event on which election is to be made")
    Options: Optional[List[OptionInstruction]] = Field(default=None, alias="Options", description="Instruction per option")

class Account(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Account key")

class BulkOptionInstruction(_FlexModel):
    AmountPct: Optional[float] = Field(default=None, alias="AmountPct", description="Quantity to be elected, in percentage")
    OptionId: Optional[str] = Field(default=None, alias="OptionId", description="Option on which election is to be made")

class SendbulkelectioninstructionsRequest(_FlexModel):
    Accounts: Optional[List[Account]] = Field(default=None, alias="Accounts", description="Accounts on which elections are to be made")
    EventId: Optional[str] = Field(default=None, alias="EventId", description="Event on which election is to be made")
    Options: Optional[List[BulkOptionInstruction]] = Field(default=None, alias="Options", description="Instruction per option for bulk election")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
