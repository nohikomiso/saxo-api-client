"""PositionClose — close-only order builders (FIFO netting / ForceOpen / ClearForceOpen).

Do NOT use MarketOrder / LimitOrder / StopOrder to close ForceOpen positions.
Those open (or net) standalone legs; FO legs need PositionId + nested Orders.
"""

from __future__ import annotations

from typing import Any, Literal

import saxo_api_client.definitions.orders as OD

from .baseorder import BaseOrder
from .helper import direction_from_amount
from .limitorder import LimitOrder
from .marketorder import MarketOrder
from .stoporder import StopOrder

CloseMode = Literal[
    "fifo_market",
    "fifo_limit",
    "fifo_stop",
    "force_open_market",
    "force_open_limit",
    "force_open_stop",
    "clear_force_open",
]


def _normalize_buy_sell(buy_sell: str | None, amount: int | float) -> str:
    if buy_sell:
        if buy_sell not in (OD.Direction.Buy, OD.Direction.Sell):
            raise ValueError(f"buy_sell must be Buy or Sell, got {buy_sell!r}")
        return buy_sell
    return direction_from_amount(amount)


def _signed_amount(amount: int | float, buy_sell: str) -> float:
    qty = abs(amount)
    return qty if buy_sell == OD.Direction.Buy else -qty


def _onfill_payload(value: dict[str, Any] | Any | None) -> dict[str, Any] | None:
    if value is None:
        return None
    if isinstance(value, dict):
        return value
    return value.data


def _nested_order_details(
    *,
    uic: int,
    amount: int | float,
    asset_type: str,
    buy_sell: str,
    order_type: str,
    manual_order: bool,
    amount_type: str,
    order_price: int | float | None = None,
    external_reference: str | None = None,
    take_profit_on_fill: dict[str, Any] | Any | None = None,
    stop_loss_on_fill: dict[str, Any] | Any | None = None,
    trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
) -> dict[str, Any]:
    details: dict[str, Any] = {
        "Uic": uic,
        "AssetType": asset_type,
        "Amount": abs(amount),
        "BuySell": buy_sell,
        "OrderType": order_type,
        "AmountType": amount_type,
        "ManualOrder": manual_order,
        "OrderDuration": {"DurationType": OD.OrderDurationType.DayOrder},
    }
    if order_price is not None:
        details["OrderPrice"] = order_price
    if external_reference:
        details["ExternalReference"] = external_reference
    tp = _onfill_payload(take_profit_on_fill)
    if tp is not None:
        details["TakeProfitOnFill"] = tp
    sl = _onfill_payload(stop_loss_on_fill)
    if sl is not None:
        details["StopLossOnFill"] = sl
    tsl = _onfill_payload(trailing_stop_loss_on_fill)
    if tsl is not None:
        details["TrailingStopLossOnFill"] = tsl
    return details


class PositionClose(BaseOrder):
    """Close-only order body. For new positions use PositionOpen.

    Prefer classmethod factories named after intent (fifo_* / force_open_* /
    clear_force_open_market). Do not construct via a bare shared close() API.
    """

    def __init__(self, *, mode: CloseMode, data: dict[str, Any]) -> None:
        super().__init__()
        self.mode: CloseMode = mode
        self._data = data

    @classmethod
    def fifo_market(
        cls,
        *,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionClose:
        """FIFO/netting flatten via opposite market (no PositionId)."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        inner = MarketOrder(
            Uic=uic,
            Amount=_signed_amount(amount, buy_sell),
            AssetType=asset_type,
            IsForceOpen=False,
            ManualOrder=manual_order,
            ExternalReference=external_reference,
            TakeProfitOnFill=take_profit_on_fill,
            StopLossOnFill=stop_loss_on_fill,
            TrailingStopLossOnFill=trailing_stop_loss_on_fill,
        )
        return cls(mode="fifo_market", data=inner.data)

    @classmethod
    def fifo_limit(
        cls,
        *,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        order_price: int | float,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionClose:
        """FIFO/netting flatten via opposite limit (no PositionId)."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        inner = LimitOrder(
            Uic=uic,
            Amount=_signed_amount(amount, buy_sell),
            AssetType=asset_type,
            OrderPrice=order_price,
            IsForceOpen=False,
            ManualOrder=manual_order,
            ExternalReference=external_reference,
            TakeProfitOnFill=take_profit_on_fill,
            StopLossOnFill=stop_loss_on_fill,
            TrailingStopLossOnFill=trailing_stop_loss_on_fill,
        )
        return cls(mode="fifo_limit", data=inner.data)

    @classmethod
    def fifo_stop(
        cls,
        *,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        order_price: int | float,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionClose:
        """FIFO/netting flatten via opposite stop (no PositionId)."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        inner = StopOrder(
            Uic=uic,
            Amount=_signed_amount(amount, buy_sell),
            AssetType=asset_type,
            OrderPrice=order_price,
            IsForceOpen=False,
            ManualOrder=manual_order,
            ExternalReference=external_reference,
            TakeProfitOnFill=take_profit_on_fill,
            StopLossOnFill=stop_loss_on_fill,
            TrailingStopLossOnFill=trailing_stop_loss_on_fill,
        )
        return cls(mode="fifo_stop", data=inner.data)

    @classmethod
    def force_open_market(
        cls,
        *,
        position_id: str,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionClose:
        """Explicit ForceOpen close: PositionId + nested Market order."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        nested = _nested_order_details(
            uic=uic,
            amount=amount,
            asset_type=asset_type,
            buy_sell=buy_sell,
            order_type=OD.OrderType.Market,
            manual_order=manual_order,
            amount_type=OD.AmountType.Quantity,
            external_reference=external_reference,
            take_profit_on_fill=take_profit_on_fill,
            stop_loss_on_fill=stop_loss_on_fill,
            trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
        )
        return cls(
            mode="force_open_market",
            data={"PositionId": position_id, "Orders": [nested]},
        )

    @classmethod
    def force_open_limit(
        cls,
        *,
        position_id: str,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        order_price: int | float,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionClose:
        """Explicit ForceOpen close: PositionId + nested Limit order."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        nested = _nested_order_details(
            uic=uic,
            amount=amount,
            asset_type=asset_type,
            buy_sell=buy_sell,
            order_type=OD.OrderType.Limit,
            manual_order=manual_order,
            amount_type=OD.AmountType.Quantity,
            order_price=order_price,
            external_reference=external_reference,
            take_profit_on_fill=take_profit_on_fill,
            stop_loss_on_fill=stop_loss_on_fill,
            trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
        )
        return cls(
            mode="force_open_limit",
            data={"PositionId": position_id, "Orders": [nested]},
        )

    @classmethod
    def force_open_stop(
        cls,
        *,
        position_id: str,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        order_price: int | float,
        manual_order: bool = True,
        external_reference: str | None = None,
        take_profit_on_fill: dict[str, Any] | Any | None = None,
        stop_loss_on_fill: dict[str, Any] | Any | None = None,
        trailing_stop_loss_on_fill: dict[str, Any] | Any | None = None,
    ) -> PositionClose:
        """Explicit ForceOpen close: PositionId + nested Stop order.

        Stop must be on the correct side of the market (e.g. sell-stop only
        after Ask has moved into profit relative to entry).
        """
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        nested = _nested_order_details(
            uic=uic,
            amount=amount,
            asset_type=asset_type,
            buy_sell=buy_sell,
            order_type=OD.OrderType.Stop,
            manual_order=manual_order,
            amount_type=OD.AmountType.Quantity,
            order_price=order_price,
            external_reference=external_reference,
            take_profit_on_fill=take_profit_on_fill,
            stop_loss_on_fill=stop_loss_on_fill,
            trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
        )
        return cls(
            mode="force_open_stop",
            data={"PositionId": position_id, "Orders": [nested]},
        )

    @classmethod
    def clear_force_open_market(
        cls,
        *,
        uic: int,
        amount: int | float,
        asset_type: str,
        buy_sell: str,
        manual_order: bool = True,
        external_reference: str | None = None,
    ) -> PositionClose:
        """Flatten FO/hedge residue with ClearForceOpen=True market."""
        buy_sell = _normalize_buy_sell(buy_sell, amount)
        data: dict[str, Any] = {
            "Uic": uic,
            "AssetType": asset_type,
            "Amount": abs(amount),
            "BuySell": buy_sell,
            "OrderType": OD.OrderType.Market,
            "AmountType": OD.AmountType.Quantity,
            "ManualOrder": manual_order,
            "ClearForceOpen": True,
            "OrderDuration": {"DurationType": OD.OrderDurationType.DayOrder},
        }
        if external_reference:
            data["ExternalReference"] = external_reference
        return cls(mode="clear_force_open", data=data)

    @property
    def data(self) -> dict[str, Any]:
        return super().data
