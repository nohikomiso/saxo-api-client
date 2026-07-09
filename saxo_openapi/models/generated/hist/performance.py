"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class AccountSummaryFieldGroup(_FlexModel):
    All: Optional[Any] = Field(default=None, alias="All", description="")
    Allocation: Optional[Any] = Field(default=None, alias="Allocation", description="")
    BenchMark: Optional[Any] = Field(default=None, alias="BenchMark", description="")
    TotalCashBalancePerCurrency: Optional[Any] = Field(default=None, alias="TotalCashBalancePerCurrency", description="")
    TotalPositionsValuePerCurrency: Optional[Any] = Field(default=None, alias="TotalPositionsValuePerCurrency", description="")
    TotalPositionsValuePerProductPerSecurity: Optional[Any] = Field(default=None, alias="TotalPositionsValuePerProductPerSecurity", description="")
    TradeActivity: Optional[Any] = Field(default=None, alias="TradeActivity", description="")
    TradeSummary: Optional[Any] = Field(default=None, alias="TradeSummary", description="")

class AccountPerformanceStandardPeriod(_FlexModel):
    AllTime: Optional[Any] = Field(default=None, alias="AllTime", description="All time account performance.")
    Month: Optional[Any] = Field(default=None, alias="Month", description="The month standard account performance.")
    Quarter: Optional[Any] = Field(default=None, alias="Quarter", description="The quarter standard account performance.")
    Year: Optional[Any] = Field(default=None, alias="Year", description="The year standard account performance.")

class PerformanceSummaryRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The account group key.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account key.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The client key.")
    FieldGroups: Optional[List[AccountSummaryFieldGroup]] = Field(default=None, alias="FieldGroups", description="The field groups.")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="From date.")
    MockDataId: Optional[str] = Field(default=None, alias="MockDataId", description="The mock data identifier.")
    StandardPeriod: Optional[AccountPerformanceStandardPeriod] = Field(default=None, alias="StandardPeriod", description="The standard period.")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="To date.")

class AccountPerformanceFieldGroup(_FlexModel):
    All: Optional[Any] = Field(default=None, alias="All", description="All Calculations")
    Balance: Optional[Any] = Field(default=None, alias="Balance", description="Balance AccountPerformance metrics.")
    Balance_AccountBalance: Optional[Any] = Field(default=None, alias="Balance_AccountBalance", description="Account Balance time series from Balance Performance")
    Balance_AccountValue: Optional[Any] = Field(default=None, alias="Balance_AccountValue", description="Account Value time series from Balance Performance")
    Balance_Accruals: Optional[Any] = Field(default=None, alias="Balance_Accruals", description="Accruals time series from Balance Performance")
    Balance_Cash: Optional[Any] = Field(default=None, alias="Balance_Cash", description="Cash time series from Balance Performance")
    Balance_CashTransfer: Optional[Any] = Field(default=None, alias="Balance_CashTransfer", description="Cash Transfer time series from Balance Performance")
    Balance_MonthlyProfitLoss: Optional[Any] = Field(default=None, alias="Balance_MonthlyProfitLoss", description="Monthly ProfitLoss time series from Balance Perfomance")
    Balance_SecurityTransfer: Optional[Any] = Field(default=None, alias="Balance_SecurityTransfer", description="Security Transfer time series from Balance Performance")
    Balance_YearlyProfitLoss: Optional[Any] = Field(default=None, alias="Balance_YearlyProfitLoss", description="Yearly ProfitLoss time series from Balance Performance")
    Benchmark: Optional[Any] = Field(default=None, alias="Benchmark", description="The benchmark performance.")
    KeyFigures: Optional[Any] = Field(default=None, alias="KeyFigures", description="Performance key figures")
    TimeWeighted: Optional[Any] = Field(default=None, alias="TimeWeighted", description="Time weighted performance metrics.")
    TimeWeighted_Accumulated: Optional[Any] = Field(default=None, alias="TimeWeighted_Accumulated", description="Accumulated Time Weighted time eries from TimeWeighted Performance")
    TimeWeighted_MonthlyReturn: Optional[Any] = Field(default=None, alias="TimeWeighted_MonthlyReturn", description="Monthly Return time series from Time Weighted Performance")
    TimeWeighted_YearlyReturn: Optional[Any] = Field(default=None, alias="TimeWeighted_YearlyReturn", description="YearlyReturnTimeSeries from Time Weighted Performance")

class PerformanceTimeseriesRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The account group key.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account key.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The client key.")
    FieldGroups: Optional[List[AccountPerformanceFieldGroup]] = Field(default=None, alias="FieldGroups", description="The field groups.")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="From date.")
    IsSdcClient: Optional[bool] = Field(default=None, alias="IsSdcClient", description="")
    MockDataId: Optional[str] = Field(default=None, alias="MockDataId", description="The mock data identifier.")
    StandardPeriod: Optional[AccountPerformanceStandardPeriod] = Field(default=None, alias="StandardPeriod", description="The standard period.")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="To date.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
