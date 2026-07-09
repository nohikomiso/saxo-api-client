"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class BookingRequestType(_FlexModel):
    BkAmountId: Optional[Any] = Field(default=None, alias="BkAmountId", description="Booking amount Id")
    CaMasterRecordId: Optional[Any] = Field(default=None, alias="CaMasterRecordId", description="Corporate action Id")
    RelatedTradeId: Optional[Any] = Field(default=None, alias="RelatedTradeId", description="Related trade Id")

class GetTradeDetailsreportfortheaccountsofaspecifiedclientRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account key.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique id of the client.")
    FilterType: Optional[BookingRequestType] = Field(default=None, alias="FilterType", description="Values which gets included in the request")
    FilterValue: Optional[str] = Field(default=None, alias="FilterValue", description="Id for the specified filter type.")
    TradeId: Optional[str] = Field(default=None, alias="TradeId", description="Trade id")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
