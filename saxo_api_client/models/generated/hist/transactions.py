"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class TransactionType(_FlexModel):
    All: Optional[Any] = Field(default=None, alias="All", description="All Transactons")
    CashAmount: Optional[Any] = Field(default=None, alias="CashAmount", description="Cash Amount")
    CashTransfer: Optional[Any] = Field(default=None, alias="CashTransfer", description="Cash transfer")
    CorporateAction: Optional[Any] = Field(default=None, alias="CorporateAction", description="Corporate Action")
    Trade: Optional[Any] = Field(default=None, alias="Trade", description="Trade")

class HistoricalTransactionsRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the resource belongs.")
    AccountKeys: Optional[List[str]] = Field(default=None, alias="AccountKeys", description="The keys of the accounts to which the resource belongs.")
    AssetTypes: Optional[str] = Field(default=None, alias="AssetTypes", description="Comma seperated asset type list to provide filterd transaction only for passed asset types.")
    BookingId: Optional[str] = Field(default=None, alias="BookingId", description="Booking id for which data is needed")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the historic data belongs.")
    CorporateActionId: Optional[str] = Field(default=None, alias="CorporateActionId", description="Corporate action id for which data is needed")
    Events: Optional[str] = Field(default=None, alias="Events", description="Comma seperated event type list to provide filterd transaction only for passed event types.")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="From date")
    FundingSubType: Optional[str] = Field(default=None, alias="FundingSubType", description="Comma seperated event type list to provide filterd transaction only for passed funding sub types.")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="To date")
    ToOpenOrClose: Optional[str] = Field(default=None, alias="ToOpenOrClose", description="Comma seperated ToOpenOrClose to provide filtered transaction only for passed ToOpen/Close/Pending.")
    TradeId: Optional[str] = Field(default=None, alias="TradeId", description="Trade id for which data is needed")
    TransactionType: Optional[TransactionType] = Field(default=None, alias="TransactionType", description="Transaction type for which trasactions are needed")
    Uics: Optional[str] = Field(default=None, alias="Uics", description="Comma seperated Uic list to provide filterd transaction only for passed Uics.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
