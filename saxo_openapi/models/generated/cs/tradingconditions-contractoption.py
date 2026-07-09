"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class ScheduledTradingConditionsFieldGroup(_FlexModel):
    ScheduledTradingConditions: Optional[Any] = Field(default=None, alias="ScheduledTradingConditions", description="Scheduled Trading Conditions")

class GettradingconditionsforacontractoptionRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account key to lookup the conditions for")
    FieldGroups: Optional[List[ScheduledTradingConditionsFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specify which field groups to return")
    OptionRootId: Optional[int] = Field(default=None, alias="OptionRootId", description="The optionRootId for the option to lookup")
    Uic: Optional[int] = Field(default=None, alias="Uic", description="The uic for the instrument to lookup")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
