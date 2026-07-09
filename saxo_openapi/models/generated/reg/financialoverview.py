"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class EntityType(_FlexModel):
    Individual: Optional[Any] = Field(default=None, alias="Individual", description="An Individual person")
    Organisation: Optional[Any] = Field(default=None, alias="Organisation", description="A corporation")

class GetthemostrecentfinancialoverviewforthespecifiedindividualororganisationRequest(_FlexModel):
    EntityKey: Optional[str] = Field(default=None, alias="EntityKey", description="Must be UserKey if EntityType=Individual or ClientKey if EntityType=Organisation")
    EntityType: Optional[EntityType] = Field(default=None, alias="EntityType", description="An individual person or organisation")

class UpdatethefinancialoverviewforthespecifiedindividualororganisationRequest(_FlexModel):
    Assets: Optional[float] = Field(default=None, alias="Assets", description="Assets held.")
    BenchmarkDebtFactor: Optional[float] = Field(default=None, alias="BenchmarkDebtFactor", description="BenchmarkDebtFactor is used in the loss ability calculation and is set by the FI depending on the clients situation.")
    BenchmarkIncomeAfterExpenses: Optional[float] = Field(default=None, alias="BenchmarkIncomeAfterExpenses", description="Benchmark benchmark income of a retail household after taxes and fixed costs has been deducted.")
    CorporateFiscalYear: Optional[int] = Field(default=None, alias="CorporateFiscalYear", description="The year of the annual statement used as the source for the numbers entered in this financial overview.")
    CorporateGuidelinesForInvesting: Optional[bool] = Field(default=None, alias="CorporateGuidelinesForInvesting", description="True, if there are any mandatory guideline for investing that the organisation must follow, for example if it's a charity or a non profit.")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency of the financial overview.")
    DebtFactor: Optional[float] = Field(default=None, alias="DebtFactor", description="Ratio of debt of a retail household divided by households yearly salary before taxes.")
    EntityKey: Optional[str] = Field(default=None, alias="EntityKey", description="Must be UserKey if EntityType=Individual or ClientKey if EntityType=Organisation")
    EntityType: Optional[EntityType] = Field(default=None, alias="EntityType", description="An individual person or organisation")
    Equity: Optional[float] = Field(default=None, alias="Equity", description="Corporate client's liquid cash")
    ExpectedEconomicChanges: Optional[bool] = Field(default=None, alias="ExpectedEconomicChanges", description="True, If the organisation expects big changes in it's financial situation, for example if they need to buy or sell any key assets.")
    Expenses: Optional[float] = Field(default=None, alias="Expenses", description="Fixed expenses.")
    IlliquidAssets: Optional[float] = Field(default=None, alias="IlliquidAssets", description="Amount of assets that are difficult to convert into cash in market.")
    Income: Optional[float] = Field(default=None, alias="Income", description="Income before taxes.")
    IncomeAfterExpenses: Optional[float] = Field(default=None, alias="IncomeAfterExpenses", description="Income after taxes and fixed costs have been deducted.")
    Liabilities: Optional[float] = Field(default=None, alias="Liabilities", description="Liabilities")
    LiquidAssets: Optional[float] = Field(default=None, alias="LiquidAssets", description="Amount of assets that can be easily converted to cash or other assets into the market.")
    NetIncome: Optional[float] = Field(default=None, alias="NetIncome", description="Corporate client's net income")
    NewCompany: Optional[bool] = Field(default=None, alias="NewCompany", description="Newly founded company without it's first annual statement")
    PensionAfterTaxes: Optional[float] = Field(default=None, alias="PensionAfterTaxes", description="Retail client's pension after taxes has been deducted.")

class PatchthefinancialoverviewforthespecifiedindividualororganisationRequest(_FlexModel):
    Assets: Optional[float] = Field(default=None, alias="Assets", description="Assets held.")
    BenchmarkDebtFactor: Optional[float] = Field(default=None, alias="BenchmarkDebtFactor", description="BenchmarkDebtFactor is used in the loss ability calculation and is set by the FI depending on the clients situation.")
    BenchmarkIncomeAfterExpenses: Optional[float] = Field(default=None, alias="BenchmarkIncomeAfterExpenses", description="Benchmark benchmark income of a retail household after taxes and fixed costs has been deducted.")
    CorporateFiscalYear: Optional[int] = Field(default=None, alias="CorporateFiscalYear", description="The year of the annual statement used as the source for the numbers entered in this financial overview.")
    CorporateGuidelinesForInvesting: Optional[bool] = Field(default=None, alias="CorporateGuidelinesForInvesting", description="True, if there are any mandatory guideline for investing that the organisation must follow, for example if it's a charity or a non profit.")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency of the financial overview.")
    DebtFactor: Optional[float] = Field(default=None, alias="DebtFactor", description="Ratio of debt of a retail household divided by households yearly salary before taxes.")
    EntityKey: Optional[str] = Field(default=None, alias="EntityKey", description="Must be UserKey if EntityType=Individual or ClientKey if EntityType=Organisation")
    EntityType: Optional[EntityType] = Field(default=None, alias="EntityType", description="An individual person or organisation")
    Equity: Optional[float] = Field(default=None, alias="Equity", description="Corporate client's liquid cash")
    ExpectedEconomicChanges: Optional[bool] = Field(default=None, alias="ExpectedEconomicChanges", description="True, If the organisation expects big changes in it's financial situation, for example if they need to buy or sell any key assets.")
    Expenses: Optional[float] = Field(default=None, alias="Expenses", description="Fixed expenses.")
    IlliquidAssets: Optional[float] = Field(default=None, alias="IlliquidAssets", description="Amount of assets that are difficult to convert into cash in market.")
    Income: Optional[float] = Field(default=None, alias="Income", description="Income before taxes.")
    IncomeAfterExpenses: Optional[float] = Field(default=None, alias="IncomeAfterExpenses", description="Income after taxes and fixed costs have been deducted.")
    Liabilities: Optional[float] = Field(default=None, alias="Liabilities", description="Liabilities")
    LiquidAssets: Optional[float] = Field(default=None, alias="LiquidAssets", description="Amount of assets that can be easily converted to cash or other assets into the market.")
    NetIncome: Optional[float] = Field(default=None, alias="NetIncome", description="Corporate client's net income")
    NewCompany: Optional[bool] = Field(default=None, alias="NewCompany", description="Newly founded company without it's first annual statement")
    PensionAfterTaxes: Optional[float] = Field(default=None, alias="PensionAfterTaxes", description="Retail client's pension after taxes has been deducted.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
