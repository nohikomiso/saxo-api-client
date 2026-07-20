"""PositionOpen — open-only order builders (new positions).

Do NOT use these classes to close existing positions. Use PositionClose.
"""

from __future__ import annotations

from typing import Any, Literal

import saxo_api_client.definitions.orders as OD

from .baseorder import BaseOrder
from .helper import direction_from_amount
from .limitorder import LimitOrder
from .marketorder import MarketOrder
from .stoplimitorder import StopLimitOrder
from .stoporder import StopOrder

OpenMode = Literal["market", "limit", "stop", "stop_limit"]


def _normalize_buy_sell(buy_sell: str | None, amount: int | float) -> str:
    if buy_sell:
        if buy_sell not in (OD.Direction.Buy, OD.Direction.Sell):
            raise ValueError(f"buy_sell must be Buy or Sell, got {buy_sell!r}")
        return buy_sell
    return direction_from_amount(amount)


def _signed_amount(amount: int | float, buy_sell: str) -> float:
    qty = abs(amount)
    return qty if buy_sell == OD.Direction.Buy else -qty


class PositionOpen(BaseOrder):
    """Open-only order body. For closing use PositionClose.

    ``is_force_open`` is mandatory (no default) so FIFO vs hedge is never guessed.
    """

    def __init__(self, *, mode: OpenMode, data: dict[str, Any]) -> None:
        super().__init__()
        self.mode: OpenMode = mode
        self._data = data

    @classmethod
    def market(
        cls,
        *,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        is_force_open: bool,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionOpen:
        """Open a new position with a market order."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        inner = MarketOrder(
            Uic=uic,
            Amount=_signed_amount(amount, buy_sell),
            AssetType=asset_type,
            IsForceOpen=is_force_open,
            ManualOrder=manual_order,
            ExternalReference=external_reference,
            TakeProfitOnFill=take_profit_on_fill,
            StopLossOnFill=stop_loss_on_fill,
            TrailingStopLossOnFill=trailing_stop_loss_on_fill,
        )
        return cls(mode="market", data=inner.data)

    @classmethod
    def limit(
        cls,
        *,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        order_price: int | float,
        is_force_open: bool,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionOpen:
        """Open a new position with a limit order."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        inner = LimitOrder(
            Uic=uic,
            Amount=_signed_amount(amount, buy_sell),
            AssetType=asset_type,
            OrderPrice=order_price,
            IsForceOpen=is_force_open,
            ManualOrder=manual_order,
            ExternalReference=external_reference,
            TakeProfitOnFill=take_profit_on_fill,
            StopLossOnFill=stop_loss_on_fill,
            TrailingStopLossOnFill=trailing_stop_loss_on_fill,
        )
        return cls(mode="limit", data=inner.data)

    @classmethod
    def stop(
        cls,
        *,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        order_price: int | float,
        is_force_open: bool,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionOpen:
        """Open a new position with a stop order (not a close)."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        inner = StopOrder(
            Uic=uic,
            Amount=_signed_amount(amount, buy_sell),
            AssetType=asset_type,
            OrderPrice=order_price,
            IsForceOpen=is_force_open,
            ManualOrder=manual_order,
            ExternalReference=external_reference,
            TakeProfitOnFill=take_profit_on_fill,
            StopLossOnFill=stop_loss_on_fill,
            TrailingStopLossOnFill=trailing_stop_loss_on_fill,
        )
        return cls(mode="stop", data=inner.data)

    @classmethod
    def stop_limit(
        cls,
        *,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        order_price: int | float,
        stop_limit_price: int | float,
        is_force_open: bool,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionOpen:
        """Open a new position with a stop-limit order."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        inner = StopLimitOrder(
            Uic=uic,
            Amount=_signed_amount(amount, buy_sell),
            AssetType=asset_type,
            OrderPrice=order_price,
            StopLimitPrice=stop_limit_price,
            IsForceOpen=is_force_open,
            ManualOrder=manual_order,
            ExternalReference=external_reference,
            TakeProfitOnFill=take_profit_on_fill,
            StopLossOnFill=stop_loss_on_fill,
            TrailingStopLossOnFill=trailing_stop_loss_on_fill,
        )
        return cls(mode="stop_limit", data=inner.data)

    @property
    def data(self) -> dict[str, Any]:
        return super().data
