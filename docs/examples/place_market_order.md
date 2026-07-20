# 成行注文発注ワークフロー

新規建ての成行は `SaxoClient.open_market`（または `PositionOpen.market`）を推奨します。
決済は [close_position.md](close_position.md) を参照。

## 前提条件

*   有効なアクセストークン

---

## 推奨: SaxoClient（新規）

```python
import json
import os
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.definitions.orders import AssetType

token = os.getenv("SAXO_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
client = SaxoClient(access_token=token)

# Stock: IsForceOpen は送信前に自動除去されるが、open_* では明示推奨
rv = client.open_market(
    symbol="AAPL",
    amount=10,
    buy_sell="Buy",
    asset_type=AssetType.Stock,
    is_force_open=False,
)
print(json.dumps(rv, indent=2))
```

レガシーの `client.market_order(...)` も利用可能ですが、意図が「新規」なら `open_market` の方が明確です。

---

## Layer 2: PositionOpen

```python
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.contrib.orders import PositionOpen

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")

order = PositionOpen.market(
    uic=21,
    amount=10000,
    asset_type="FxSpot",
    buy_sell="Buy",
    is_force_open=True,  # 両建て新規
)
rv = client.place_order(order)
print(f"OrderId: {rv['OrderId']}")
```

低レベル `MarketOrder` / `MarketOrderFxSpot` を使う場合も `IsForceOpen` は必須です。

## 解説

1. **新規 vs 決済**: 同じ成行でも決済は `PositionClose` / `close_fifo_*` / `close_force_open_*`。
2. **ForceOpen**: 決済に standalone Market/Stop を使うと偽決済（反対新規）になる → [contrib/orders.md](../contrib/orders.md)。
