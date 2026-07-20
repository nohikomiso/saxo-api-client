# Trading Orders

> **パラメータ詳細は MCP へ**: `get_saxo_endpoint_spec("POST", "/trade/v2/orders")` 等。
> 注文の**意図別**組み立ては [contrib/orders.md](../../contrib/orders.md)（`PositionOpen` / `PositionClose`）。
> このファイルは Python バインディング索引です。

`saxo_api_client.endpoints.trading.orders`

| クラス | Method | Path |
|--------|--------|------|
| `Order` | POST | `/trade/v2/orders` |
| `ChangeOrder` | PATCH | `/trade/v2/orders` |
| `CancelOrders` | DELETE | `/trade/v2/orders/{OrderIds}` |
| `PrecheckOrder` | POST | `/trade/v2/orders/precheck` |

## 推奨（ライブラリ）

```python
from saxo_api_client.contrib.client import SaxoClient

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")
# 新規
client.open_market(asset_type="FxSpot", uic=21, amount=10000, buy_sell="Buy", is_force_open=False)
# 決済は examples/close_position.md
```

## 低レベル例

```python
import saxo_api_client.endpoints.trading as tr
from saxo_api_client import API

client = API(access_token="YOUR_ACCESS_TOKEN")
r = tr.orders.PrecheckOrder(data={...})  # ボディ詳細は MCP
client.request(r)
```

## スキーマ

- [order_body.json](../../schemas/trading/orders/order_body.json)
- [order_response.json](../../schemas/trading/orders/order_response.json)
