#!/usr/bin/env python3

"""
Order Validation (PreCheck) Sample

Demonstrates SaxoClient.validate_order without placing an actual order.

Usage:
    uv run libs/saxo_api_client/samples/verify_orders_precheck.py
"""

import json

import saxo_api_client.definitions.orders as OD
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.contrib.orders import MarketOrder, StopOrder


def read_token(token_file="token_demo.txt"):
    with open(token_file) as f:
        return f.read().strip()


def main():
    try:
        token = read_token("token_demo.txt")
        client = SaxoClient(access_token=token)

        print("--- Verifying PreCheck (Validation) ---")
        print(f"AccountKey: {client.account_key}")

        order_spec = MarketOrder(
            Uic=21,
            Amount=1000,
            AssetType=OD.AssetType.FxSpot,
            IsForceOpen=True,
            ManualOrder=True,
        )

        print("1. Validating Valid Order (Market)...")
        try:
            rv = client.validate_order(order_spec)
            print(f"   PreCheck Result: {json.dumps(rv, indent=2)}")
            print("   SUCCESS: Order validated.")
        except Exception as e:
            print(f"   FAILED: {e}")

        print("\n2. Validating Invalid Order (Buy Stop @ 0.0001)...")
        invalid_spec = StopOrder(
            Uic=21,
            Amount=1000,
            OrderPrice=0.0001,
            AssetType=OD.AssetType.FxSpot,
            IsForceOpen=True,
            ManualOrder=True,
        )

        try:
            rv = client.validate_order(invalid_spec)
            print(f"   PreCheck Result: {json.dumps(rv, indent=2)}")
            if "ErrorInfo" in rv:
                print(f"   SUCCESS: Validation caught error: {rv['ErrorInfo']}")
            else:
                print("   Passed validation (Unexpected for near-zero price but ok for test flow)")
        except Exception as e:
            print(f"   SUCCESS: API Raised Exception: {e}")

    except Exception as e:
        print(f"Main execution error: {e}")


if __name__ == "__main__":
    main()
