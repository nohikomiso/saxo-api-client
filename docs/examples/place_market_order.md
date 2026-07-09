# 成行注文発注ワークフロー

この例では、`SaxoTrader` (Layer 3) を使用して、最も簡単かつ安全に成行注文を発注する方法を示します。

## 前提条件

*   有効なアクセストークン

---

## 推奨アプローチ: SaxoTrader (Layer 3) の使用

`SaxoTrader` を使うと、AccountKey の自動注入やティッカーシンボル（Symbol）から UIC への自動変換が行われ、SaxoBank API の複雑な仕様を完全に隠蔽できます。

```python
import json
import os
from saxo_api_client import API
from saxo_api_client.contrib.trader import SaxoTrader
from saxo_api_client.definitions.orders import AssetType

# 1. クライアントの初期化
token = os.getenv("SAXO_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
client = API(access_token=token)

# 2. SaxoTrader の初期化 (AccountKey は自動取得されます)
trader = SaxoTrader(client)

# 3. 注文の実行 (Symbol で注文可能)
try:
    print("--- 🍎 AAPL 株の成行注文 ---")
    # UIC(識別番号)を知らなくても Symbol で指定可能
    rv = trader.market_order(
        Symbol="AAPL",
        Amount=10,
        AssetType=AssetType.Stock
    )
    print("注文成功:")
    print(json.dumps(rv, indent=2))
    
except Exception as e:
    print(f"注文失敗: {e}")
```

---

## 中級者向け: Order Builders (Layer 2) の使用

特殊な注文を自力で組み立てたい場合は、`contrib.orders` モジュールの Order Builder を使用して注文パラメーター（辞書）を構築し、生のAPIエンドポイントに渡します。
※ このレイヤーでは UIC (`Uic`) を直接指定し、`AccountKey` を明示的に注入する必要があります。

```python
import json
from saxo_api_client import API
import saxo_api_client.endpoints.trading as tr
from saxo_api_client.contrib.orders import (
    MarketOrderFxSpot,
    tie_account_to_order
)
from saxo_api_client.contrib.session import account_info

client = API(access_token="YOUR_ACCESS_TOKEN")

# 1. アカウント情報の取得
AccountKey = account_info(client).AccountKey

# 2. 注文スペックの作成 (例: EURUSD の UIC は 21)
order_spec = MarketOrderFxSpot(
    Uic=21,
    Amount=10000
)

# 3. アカウントの紐付け
order_spec = tie_account_to_order(AccountKey, order_spec)

# 4. リクエストの実行
r = tr.orders.Order(data=order_spec)
try:
    rv = client.request(r)
    print(f"OrderId: {rv['OrderId']}")
except Exception as e:
    print(f"注文失敗: {e}")
```

## 解説

1. **Layer 3**: `SaxoTrader.market_order()` は内部で `InstrumentToUic` を呼び出し、`AAPL` のようなティッカーから `Uic` を自動で検索します。もし複数ヒットした場合でも、`PrimaryListing` を用いて自動で本家取引所（例: NASDAQ）の銘柄に絞り込みます。
2. **Layer 2**: `MarketOrderFxSpot` は辞書（Dict）を生成するヘルパーです。SaxoBankの APIエンドポイント (`tr.orders.Order`) はこの辞書を受け取り、裏側で **Layer 1** の `TradeOrdersRequest` Pydanticモデルによるバリデーションを行ってから送信します。
