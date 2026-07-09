"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class AmountTypeSource(_FlexModel):
    CorporateAction: Optional[Any] = Field(default=None, alias="CorporateAction", description="Accruals derived from corporate action bookings")
    Financing: Optional[Any] = Field(default=None, alias="Financing", description="Accruals derived from financing and fee bookings")
    TransactionsNotBooked: Optional[Any] = Field(default=None, alias="TransactionsNotBooked", description="Intraday transactions that have not been booked")

class UnsettledAmountRequestType(_FlexModel):
    AmountTypes: Optional[Any] = Field(default=None, alias="AmountTypes", description="Amount Types")
    Currencies: Optional[Any] = Field(default=None, alias="Currencies", description="Currencies")

class CurrencyBreakdownOwedbyCurrencyandAmountTypeRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the resource belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The keys of the accounts to which the resource belongs.")
    AmountTypeSource: Optional[AmountTypeSource] = Field(default=None, alias="AmountTypeSource", description="Specifies the response data granularity, providing access to source of AmountType.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the resource belongs.")
    CurrencyCode: Optional[Any] = Field(default=None, alias="CurrencyCode", description="Data will be filtered for account currency")
    Scope: Optional[UnsettledAmountRequestType] = Field(default=None, alias="Scope", description="Specifies the response data granularity, providing access to either Currencies(default) or AmountTypes.")

class ExchangeBreakdownOwedbyExchangeandCurrencyRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the resource belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The keys of the accounts to which the resource belongs.")
    AmountTypeSource: Optional[AmountTypeSource] = Field(default=None, alias="AmountTypeSource", description="Specifies the response data granularity, providing access to source of AmountType.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the resource belongs.")

class ExchangeBreakdownOwedbyCurrencyandAmountTypeRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the resource belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The keys of the accounts to which the resource belongs.")
    AmountTypeSource: Optional[AmountTypeSource] = Field(default=None, alias="AmountTypeSource", description="Specifies the response data granularity, providing access to source of AmountType.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the resource belongs.")
    ExchangeId: Optional[str] = Field(default=None, alias="ExchangeId", description="The exchange identifier for which value dated amounts is requested. If no exchange is associated to those amounts, use 'NoExchange' as the value.")

class CurrencyBreakdownOwedbyInstrumentRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the resource belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The keys of the accounts to which the resource belongs.")
    AmountTypeId: Optional[str] = Field(default=None, alias="AmountTypeId", description="Amount Type Id of the owed amount, for which you want instruments returned.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the resource belongs.")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency code of the owed amount, for which you want instruments returned.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
