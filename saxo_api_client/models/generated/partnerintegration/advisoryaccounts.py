"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetadvisoryaccountsforspecifiedclientRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")

class ClientEntityType(_FlexModel):
    Individual: Optional[Any] = Field(default=None, alias="Individual", description="Individual Type - enum")
    Organisation: Optional[Any] = Field(default=None, alias="Organisation", description="Organisation Type - enum")

class ManagementType(_FlexModel):
    Advisory: Optional[Any] = Field(default=None, alias="Advisory", description="Advisory")
    Discretionary: Optional[Any] = Field(default=None, alias="Discretionary", description="Discretionary")
    TradeAdvisory: Optional[Any] = Field(default=None, alias="TradeAdvisory", description="TradeAdvisory")

class PartnerTaxEnvironment(_FlexModel):
    ChildSavings: Optional[Any] = Field(default=None, alias="ChildSavings", description="ChildSavings")
    CompanyTaxScheme: Optional[Any] = Field(default=None, alias="CompanyTaxScheme", description="Company tax scheme")
    Corporate: Optional[Any] = Field(default=None, alias="Corporate", description="Corporate")
    EstablishmentAccount: Optional[Any] = Field(default=None, alias="EstablishmentAccount", description="EstablishmentAccount")
    FreeCash: Optional[Any] = Field(default=None, alias="FreeCash", description="FreeCash")
    InvestmentSavingsAccount: Optional[Any] = Field(default=None, alias="InvestmentSavingsAccount", description="InvestmentSavingsAccount")
    None_: Optional[Any] = Field(default=None, alias="None", description="None")
    Pension: Optional[Any] = Field(default=None, alias="Pension", description="Pension")

class CreateadvisoryaccountsforspecifiedclientRequest(_FlexModel):
    AccountName: Optional[str] = Field(default=None, alias="AccountName", description="Account name")
    AccountTemplate: Optional[str] = Field(default=None, alias="AccountTemplate", description="Account template")
    AdvisoryAccountId: Optional[int] = Field(default=None, alias="AdvisoryAccountId", description="Identifier for Advisory Accounts")
    ClientEntityType: Optional[ClientEntityType] = Field(default=None, alias="ClientEntityType", description="Client Entity Type - enum")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency of the client's account")
    IsGuaranteeNoteAccount: Optional[bool] = Field(default=None, alias="IsGuaranteeNoteAccount", description="Boolean for Allowing Guarantee Notes")
    IsMainAccount: Optional[bool] = Field(default=None, alias="IsMainAccount", description="Boolean for Main Account")
    ManagementType: Optional[ManagementType] = Field(default=None, alias="ManagementType", description="Management Type - enum")
    PartnerTaxEnvironment: Optional[PartnerTaxEnvironment] = Field(default=None, alias="PartnerTaxEnvironment", description="Partner Tax Environment - enum")
    SecuritiesAccountTemplate: Optional[str] = Field(default=None, alias="SecuritiesAccountTemplate", description="Securities Account Template")
    SortOrder: Optional[int] = Field(default=None, alias="SortOrder", description="Sort Order")

class UpdateadvisoryaccountsforspecifiedclientsadvisoryaccountRequest(_FlexModel):
    AccountName: Optional[str] = Field(default=None, alias="AccountName", description="Account name")
    AccountTemplate: Optional[str] = Field(default=None, alias="AccountTemplate", description="Account template")
    AdvisoryAccountId: Optional[int] = Field(default=None, alias="AdvisoryAccountId", description="")
    ClientEntityType: Optional[ClientEntityType] = Field(default=None, alias="ClientEntityType", description="Client Entity Type - enum")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency of the client's account")
    IsGuaranteeNoteAccount: Optional[bool] = Field(default=None, alias="IsGuaranteeNoteAccount", description="Boolean for Allowing Guarantee Notes")
    IsMainAccount: Optional[bool] = Field(default=None, alias="IsMainAccount", description="Boolean for Main Account")
    ManagementType: Optional[ManagementType] = Field(default=None, alias="ManagementType", description="Management Type - enum")
    PartnerTaxEnvironment: Optional[PartnerTaxEnvironment] = Field(default=None, alias="PartnerTaxEnvironment", description="Partner Tax Environment - enum")
    SecuritiesAccountTemplate: Optional[str] = Field(default=None, alias="SecuritiesAccountTemplate", description="Securities Account Template")
    SortOrder: Optional[int] = Field(default=None, alias="SortOrder", description="Sort Order")

class DeletespecifiedclientsadvisoryaccountRequest(_FlexModel):
    AdvisoryAccountId: Optional[int] = Field(default=None, alias="AdvisoryAccountId", description="")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
