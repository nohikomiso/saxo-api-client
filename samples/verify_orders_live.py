#!/usr/bin/env python3

"""
Live Order Verification Sample

Demonstrates order placement via SaxoClient (Layer 3):
- Limit Orders
- Stop Orders (Smart Routing)
- Stop Limit Orders

Usage:
    uv run libs/saxo_api_client/samples/verify_orders_live.py
"""

import time

import saxo_api_client.definitions.orders as OD
from saxo_api_client.contrib.client import SaxoClient


def read_token(token_file="token_demo.txt"):
    with open(token_file) as f:
        return f.read().strip()


def get_current_price(client: SaxoClient, uic: int, asset_type: str) -> float:
    try:
        res = client.get_prices(asset_type=asset_type, uic=uic)
        quote = res.get("Quote", {})
        bid = quote.get("Bid")
        ask = quote.get("Ask")
        mid = (bid + ask) / 2 if bid and ask else None
        print(f"   [Market Data] {asset_type} (UIC {uic}): Bid={bid}, Ask={ask}, Mid={mid}")
        return mid if mid else 0.0
    except Exception as e:
        print(f"   [Market Data] Failed to fetch price: {e}")
        return 0.0


def place_orders(client: SaxoClient, name: str, uic: int, asset_type: str, default_price: float) -> None:
    print(f"\n=== Testing {name} (UIC: {uic}, Asset: {asset_type}) ===")

    current_price = get_current_price(client, uic, asset_type)
    if current_price == 0.0:
        print(f"   Using default price estimate: {default_price}")
        current_price = default_price

    amount = 1000 if asset_type == OD.AssetType.FxSpot else 1

    limit_price = current_price * 0.95
    if asset_type == OD.AssetType.FxSpot:
        limit_price = current_price - 0.0050
    limit_price = round(limit_price, 4 if asset_type == OD.AssetType.FxSpot else 2)

    print(f"1. Placing Limit Order (Buy @ {limit_price})...")
    try:
        r = client.limit_order(
            asset_type=asset_type,
            amount=amount,
            order_price=limit_price,
            uic=uic,
            IsForceOpen=True,
            ManualOrder=True,
        )
        print(f"   SUCCESS: OrderId={r['OrderId']}")
    except Exception as e:
        print(f"   FAILED: {e}")

    time.sleep(1)

    stop_price = current_price * 1.05
    if asset_type == OD.AssetType.FxSpot:
        stop_price = current_price + 0.0050
    stop_price = round(stop_price, 4 if asset_type == OD.AssetType.FxSpot else 2)

    print(f"2. Placing Stop Order (Smart Routing, Buy Stop @ {stop_price})...")
    try:
        r = client.stop_order(
            asset_type=asset_type,
            amount=amount,
            order_price=stop_price,
            uic=uic,
            IsForceOpen=True,
            ManualOrder=True,
        )
        print(f"   SUCCESS: OrderId={r['OrderId']}")
    except Exception as e:
        print(f"   FAILED: {e}")

    time.sleep(1)

    sl_trigger = stop_price
    sl_limit = stop_price * 1.01
    if asset_type == OD.AssetType.FxSpot:
        sl_limit = stop_price + 0.0010
    sl_limit = round(sl_limit, 4 if asset_type == OD.AssetType.FxSpot else 2)

    print(f"3. Placing Stop Limit Order (Trigger @ {sl_trigger}, Limit @ {sl_limit})...")
    try:
        r = client.stop_limit_order(
            asset_type=asset_type,
            amount=amount,
            order_price=sl_trigger,
            stop_limit_price=sl_limit,
            uic=uic,
            IsForceOpen=True,
            ManualOrder=True,
        )
        print(f"   SUCCESS: OrderId={r['OrderId']}")
    except Exception as e:
        print(f"   FAILED: {e}")

    time.sleep(1)


def main():
    try:
        token = read_token("token_demo.txt")
        client = SaxoClient(access_token=token)

        print(f"AccountKey: {client.account_key}")

        place_orders(client, "FX Spot (EURUSD)", 21, OD.AssetType.FxSpot, 1.05)
        place_orders(client, "Stock (AAPL)", 211, OD.AssetType.Stock, 200.0)
        place_orders(client, "CFD on Stock (AAPL)", 211, OD.AssetType.CfdOnStock, 200.0)

    except Exception as e:
        print(f"Main execution error: {e}")


if __name__ == "__main__":
    main()
