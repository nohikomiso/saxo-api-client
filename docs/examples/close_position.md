# ポジション決済ワークフロー

この例では、保有しているポジションを決済（クローズ）する方法を示します。
**新規** は `PositionOpen`、**決済** は `PositionClose` を使います（同じ指値・逆指値でもクラスが違う）。

## 前提条件

*   有効なアクセストークン
*   FIFO か ForceOpen かの判断
*   ForceOpen の場合: `PositionId`（`iter_open_positions` / PositionsQuery トップレベル）

## ForceOpen 明示成行クローズ

```python
from saxo_api_client.contrib.client import SaxoClient

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")
rows = client.iter_open_positions(uic=42, asset_type="FxSpot")
row = next(r for r in rows if r["is_force_open"])
client.close_force_open_market(
    position_id=row["position_id"],
    asset_type="FxSpot",
    uic=42,
    amount=abs(row["amount"]),
    buy_sell="Sell" if row["amount"] > 0 else "Buy",
)
```

## FIFO 相殺成行

```python
client.close_fifo_market(
    asset_type="FxSpot",
    uic=42,
    amount=10000,
    buy_sell="Sell",
)
```

## Layer 2 ビルダー直接

```python
from saxo_api_client.contrib.orders import PositionClose, tie_account_to_order
import saxo_api_client.endpoints.trading as tr
from saxo_api_client import API

api = API(access_token="YOUR_ACCESS_TOKEN")
pc = PositionClose.force_open_stop(
    position_id="12345678",
    uic=42,
    amount=10000,
    asset_type="FxSpot",
    buy_sell="Sell",
    order_price=150.25,
)
body = tie_account_to_order(account_key, pc)
api.request(tr.orders.Order(data=body))
```

## 禁止

*   ForceOpen を standalone `StopOrder` / `LimitOrder` で「閉じる」（実際は反対新規）
*   マスターにだけ `PositionId` を付ける（入れ子 `Orders[]` が必要）
