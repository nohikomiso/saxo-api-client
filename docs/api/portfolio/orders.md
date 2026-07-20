# Portfolio Orders

> **パラメータ詳細は MCP へ**。このファイルは Python バインディング索引です。
> 注文の**発注**は Trading Orders / [contrib/orders.md](../../contrib/orders.md)。ここはオープン注文の**照会**。

`saxo_api_client.endpoints.portfolio.orders`

| クラス | Method | Path |
|--------|--------|------|
| `GetOpenOrder` | GET | `/port/v1/orders/{ClientKey}/{OrderId}` |
| `GetOpenOrdersMe` | GET | `/port/v1/orders/me` |
| `OrderDetails` | GET | `/port/v1/orders/{OrderId}/details` |
| `GetAllOpenOrders` | GET | `/port/v1/orders` |
| `CreateOpenOrdersSubscription` | POST | `/port/v1/orders/subscriptions` |
| `RemoveOpenOrderSubscriptionsByTag` | DELETE | subscriptions by tag |
| `RemoveOpenOrderSubscription` | DELETE | one subscription |

## 最小例

```python
from saxo_api_client.contrib.client import SaxoClient

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")
print(client.get_open_orders())
```

## スキーマ

[schemas/portfolio/orders/](../../schemas/portfolio/orders/)
