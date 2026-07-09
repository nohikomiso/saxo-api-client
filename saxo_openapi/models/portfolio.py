"""
Saxo OpenAPI Pydantic Models - Portfolio.
"""
from typing import Literal, Optional
from pydantic import Field

from .base import _FlexModel


class _Greeks(_FlexModel):
    InstrumentDelta: Optional[float] = None
    InstrumentGamma: Optional[float] = None
    InstrumentTheta: Optional[float] = None
    InstrumentThetaInAccountCurrency: Optional[float] = None
    InstrumentVega: Optional[float] = None
    MidVol: Optional[float] = None
    TheoreticalPrice: Optional[float] = None

_Greeks.model_rebuild()


class _OptionDetails(_FlexModel):
    CanBeExercised: Optional[bool] = None
    ExerciseStyle: Optional[str] = None
    ExpiryDate: Optional[str] = None
    PutCall: Optional[Literal["Put", "Call"]] = None
    SettlementStyle: Optional[str] = None
    Strike: Optional[float] = None

_OptionDetails.model_rebuild()


class _PositionBase(_FlexModel):
    AccountId: str
    AccountKey: str
    Amount: float
    AssetType: str
    CanBeClosed: bool = False
    Uic: int
    OpenPrice: Optional[float] = None
    OpenPriceIncludingCosts: Optional[float] = None
    Status: str = "Unknown"
    OptionsData: Optional[_OptionDetails] = None

_PositionBase.model_rebuild()


class _PositionView(_FlexModel):
    CalculationReliability: Optional[str] = None
    CurrentPrice: Optional[float] = None
    ExposureCurrency: Optional[str] = None
    ProfitLossOnTrade: Optional[float] = None

_PositionView.model_rebuild()


class _DisplayAndFormat(_FlexModel):
    Currency: str
    Decimals: Optional[int] = None
    Description: Optional[str] = None
    Symbol: Optional[str] = None

_DisplayAndFormat.model_rebuild()


class SaxoPosition(_FlexModel):
    """
    Saxo /port/v1/positions/me の単一レコードモデル
    """
    PositionId: str
    NetPositionId: Optional[str] = None
    PositionBase: Optional[_PositionBase] = None
    Greeks: Optional[_Greeks] = None
    PositionView: Optional[_PositionView] = None
    DisplayAndFormat: Optional[_DisplayAndFormat] = None

SaxoPosition.model_rebuild()


class PositionsMeResponse(_FlexModel):
    """
    /port/v1/positions/me のトップレベルレスポンスモデル
    """
    Data: list[SaxoPosition] = Field(default_factory=list)

PositionsMeResponse.model_rebuild()
