"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GettheexternalaccountsdetailslistRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="")

class PartnerTaxEnvironment(_FlexModel):
    ChildSavings: Optional[Any] = Field(default=None, alias="ChildSavings", description="ChildSavings")
    CompanyTaxScheme: Optional[Any] = Field(default=None, alias="CompanyTaxScheme", description="Company tax scheme")
    Corporate: Optional[Any] = Field(default=None, alias="Corporate", description="Corporate")
    EstablishmentAccount: Optional[Any] = Field(default=None, alias="EstablishmentAccount", description="EstablishmentAccount")
    FreeCash: Optional[Any] = Field(default=None, alias="FreeCash", description="FreeCash")
    InvestmentSavingsAccount: Optional[Any] = Field(default=None, alias="InvestmentSavingsAccount", description="InvestmentSavingsAccount")
    None_: Optional[Any] = Field(default=None, alias="None", description="None")
    Pension: Optional[Any] = Field(default=None, alias="Pension", description="Pension")

class ExternalAccountExtention(_FlexModel):
    AccountName: Optional[str] = Field(default=None, alias="AccountName", description="Account name")
    AccountNumber: Optional[str] = Field(default=None, alias="AccountNumber", description="Account number")
    AllowUserEdit: Optional[bool] = Field(default=None, alias="AllowUserEdit", description="AllowUserEdit")
    AvailableForFunding: Optional[bool] = Field(default=None, alias="AvailableForFunding", description="Available for funding")
    Balance: Optional[float] = Field(default=None, alias="Balance", description="Account balance")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency of the client's account")
    IssuerBankInfo: Optional[str] = Field(default=None, alias="IssuerBankInfo", description="Issuer bank")
    OwnershipPercentage: Optional[float] = Field(default=None, alias="OwnershipPercentage", description="Partner Ownership percentage")
    PartnerTaxEnvironment: Optional[PartnerTaxEnvironment] = Field(default=None, alias="PartnerTaxEnvironment", description="Partner tax environment")

class CreateexternalaccountsRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    ExternalAccounts: Optional[List[ExternalAccountExtention]] = Field(default=None, alias="ExternalAccounts", description="Create client external accounts")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="")

class UpdateexternalaccountslistRequest(_FlexModel):
    AccountName: Optional[str] = Field(default=None, alias="AccountName", description="Account name")
    AccountNumber: Optional[str] = Field(default=None, alias="AccountNumber", description="Account number")
    AllowUserEdit: Optional[bool] = Field(default=None, alias="AllowUserEdit", description="AllowUserEdit")
    AvailableForFunding: Optional[bool] = Field(default=None, alias="AvailableForFunding", description="Available for funding")
    Balance: Optional[float] = Field(default=None, alias="Balance", description="Account balance")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency of the client's account")
    ExternalAccountIdentifier: Optional[int] = Field(default=None, alias="ExternalAccountIdentifier", description="")
    IssuerBankInfo: Optional[str] = Field(default=None, alias="IssuerBankInfo", description="Issuer bank")

class DeleteanexternalaccountRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    ExternalAccountIdentifier: Optional[int] = Field(default=None, alias="ExternalAccountIdentifier", description="")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
