# 成行注文発注ワークフロー

この例では、`SaxoClient` (Layer 3) を使用して成行注文を発注します。

## 前提条件

*   有効なアクセストークン

---

## 推奨アプローチ: SaxoClient (Layer 3)

`SaxoClient` は AccountKey の自動注入と Symbol→UIC 解決を行います。旧 `SaxoTrader` は削除済みです。

```python
import json
import os
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.definitions.orders import AssetType

token = os.getenv("SAXO_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
client = SaxoClient(access_token=token)

try:
    print("--- AAPL 株の成行注文 ---")
    rv = client.market_order(
        symbol="AAPL",
        amount=10,
        asset_type=AssetType.Stock,
    )
    print("注文成功:")
    print(json.dumps(rv, indent=2))
except Exception as e:
    print(f"注文失敗: {e}")
```

---

## 中級者向け: Order Builders (Layer 2)

特殊な注文を自力で組み立てる場合は `contrib.orders` で辞書を構築し、`SaxoClient.place_order` または生エンドポイントへ渡します。

```python
import json
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.contrib.orders import MarketOrderFxSpot

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")

order_spec = MarketOrderFxSpot(
    Uic=21,
    Amount=10000,
    IsForceOpen=True,
)

try:
    rv = client.place_order(order_spec)
    print(f"OrderId: {rv['OrderId']}")
except Exception as e:
    print(f"注文失敗: {e}")
```

## 解説

1. **Layer 3**: `SaxoClient.market_order()` は内部で `InstrumentToUic` を呼び出し、ティッカーから `Uic` を解決します。
2. **Layer 2**: `MarketOrderFxSpot` は辞書を生成するヘルパーです。送信前に Layer 1 の FlexModel バリデーションが走ります。
