# SaxoClient Helper

`saxo_api_client.contrib.client.SaxoClient` は、FX / Stock / CFD 向けの **Layer 3 ファサード**です。
`AccountKey` 注入・UIC 解決・注文実行／precheck を 1 クラスにまとめます。

> 旧 `SaxoTrader`（`contrib.trader`）は削除済みです。互換 shim はありません。本ドキュメントを正とします。

## 初期化

`access_token` または `SaxoAuthClient` を渡します。`AccountKey` は初回利用時に自動取得されます。

```python
from saxo_api_client.contrib.client import SaxoClient

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")
print(client.account_key)
```

## 注文メソッド

数量（`amount`）の符号で売買方向が決まります（正=Buy、負=Sell）。

### 成行 (Market)

```python
response = client.market_order(asset_type="FxSpot", uic=21, amount=10000)
```

### 指値 (Limit)

```python
response = client.limit_order(
    asset_type="FxSpot",
    uic=21,
    amount=10000,
    order_price=1.1025,
)
```

### 逆指値 (Stop) — スマートルーティング

銘柄の `SupportedOrderTypes` に応じて `Stop` / `StopIfTraded` を選択します。

```python
response = client.stop_order(
    asset_type="FxSpot",
    uic=21,
    amount=-10000,
    order_price=1.1000,
)
```

明示的に StopIfTraded が必要な場合:

```python
response = client.stop_if_traded_order(
    asset_type="CfdOnStock",
    uic=211,
    amount=-1,
    order_price=150.0,
)
```

### ストップリミット (StopLimit)

```python
response = client.stop_limit_order(
    asset_type="CfdOnStock",
    uic=211,
    amount=-1,
    order_price=150.0,
    stop_limit_price=149.5,
)
```

### 事前チェック (validate_order)

実発注せず `PrecheckOrder` を呼びます。

```python
from saxo_api_client.contrib.orders import LimitOrder

spec = LimitOrder(
    Uic=21,
    Amount=10000,
    OrderPrice=1.1025,
    AssetType="FxSpot",
    IsForceOpen=True,
)
result = client.validate_order(spec)
print(result.get("PreCheckResult"))
```

## IsForceOpen

- **Stock**: API 非対応のため、`SaxoClient` が送信前に自動除去します。
- **CFD / FX**: `IsForceOpen=True` で両建て可能です。

## 関連

- [option_trader.md](option_trader.md) — オプション取引用 Layer 3
- [orders.md](orders.md) — Layer 2 注文ビルダー
