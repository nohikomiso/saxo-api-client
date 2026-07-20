# 指値注文発注ワークフロー

新規建ての指値は `PositionOpen.limit`（または `SaxoClient.open_limit`）を使います。
決済の指値は [close_position.md](close_position.md) / [contrib/orders.md](../contrib/orders.md) を参照（クラスが違う）。

## 前提条件

*   有効なアクセストークン

## 推奨: SaxoClient

```python
import json
import os
from saxo_api_client.contrib.client import SaxoClient

client = SaxoClient(access_token=os.getenv("SAXO_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN"))

rv = client.open_limit(
    asset_type="FxSpot",
    uic=21,
    amount=10000,
    buy_sell="Buy",
    order_price=1.0500,
    is_force_open=False,  # 必須（FIFO）。両建てなら True
)
print(json.dumps(rv, indent=2))
```

## Layer 2: PositionOpen

```python
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.contrib.orders import PositionOpen

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")
order = PositionOpen.limit(
    uic=21,
    amount=10000,
    asset_type="FxSpot",
    buy_sell="Buy",
    order_price=1.0500,
    is_force_open=False,
)
rv = client.place_order(order)
print(rv.get("OrderId"))
```

## 解説

1. `is_force_open` は省略不可（FIFO=`False` / 両建て=`True`）。
2. 低レベル `LimitOrder` / `LimitOrderFxSpot` を使う場合も `IsForceOpen` は必須。
3. ForceOpen 建玉の**決済**に standalone Limit を使わないこと → [close_position.md](close_position.md)。
