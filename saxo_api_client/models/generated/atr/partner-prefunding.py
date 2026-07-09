"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class CreditclientaccountbasedonpreadviceRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Client account key in which fund will be deposited")
    Amount: Optional[float] = Field(default=None, alias="Amount", description="Funding Amount")
    BIC: Optional[str] = Field(default=None, alias="BIC", description="BIC (Swift Code) code of sender bank")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="ClientKey for which system will execute deposit")
    ClientName: Optional[str] = Field(default=None, alias="ClientName", description="Client Name for which system will execute deposit")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Funding currency")
    ExpectedValueDate: Optional[str] = Field(default=None, alias="ExpectedValueDate", description="Expected value date")
    ExternalReference: Optional[str] = Field(default=None, alias="ExternalReference", description="Reference number, if any")
    Iban: Optional[str] = Field(default=None, alias="Iban", description="Client International Bank Account Number")
    RemitterAccount: Optional[str] = Field(default=None, alias="RemitterAccount", description="Remitter Account")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
