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

## 推奨: 意図別 open / close

新規と決済はメソッド名で分離する（`is_force_open` / `position_id` を推測させない）。

```python
# 新規（両建て）
client.open_market(
    asset_type="FxSpot", uic=42, amount=10000, buy_sell="Buy", is_force_open=True,
)

# FO 建玉一覧（position_id はトップレベル正規化）
rows = client.iter_open_positions(uic=42)
pid = rows[0]["position_id"]

# FO 明示成行クローズ
client.close_force_open_market(
    position_id=pid, asset_type="FxSpot", uic=42, amount=10000, buy_sell="Sell",
)

# FO 明示逆指値クローズ（含み益側のみ）
client.close_force_open_stop(
    position_id=pid, asset_type="FxSpot", uic=42, amount=10000,
    buy_sell="Sell", order_price=150.25,
)

# FIFO 相殺
client.close_fifo_market(
    asset_type="FxSpot", uic=42, amount=10000, buy_sell="Sell",
)

# FO 残骸一掃
client.flatten_force_open(asset_type="FxSpot", uic=42)
```

| メソッド | 用途 |
|----------|------|
| `open_market` / `open_limit` / `open_stop` / `open_stop_limit` | 新規（`is_force_open` 必須） |
| `close_fifo_market` / `close_fifo_limit` / `close_fifo_stop` | FIFO 決済 |
| `close_force_open_market` / `close_force_open_limit` / `close_force_open_stop` | FO 明示決済 |
| `flatten_force_open` | ClearForceOpen 一掃 |
| `iter_open_positions` | PositionId 正規化一覧 |

曖昧な `close_position()` は提供しない。

## レガシー注文メソッド

数量（`amount`）の符号で売買方向が決まります（正=Buy、負=Sell）。FO クローズには使わない。

### 成行 (Market)

```python
response = client.market_order(asset_type="FxSpot", uic=21, amount=10000, IsForceOpen=False)
```

### 指値 (Limit)

```python
response = client.limit_order(
    asset_type="FxSpot",
    uic=21,
    amount=10000,
    order_price=1.1025,
    IsForceOpen=False,
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
    IsForceOpen=False,
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
    IsForceOpen=False,
)
```

### 事前チェック (validate_order)

```python
from saxo_api_client.contrib.orders import PositionClose

spec = PositionClose.force_open_market(
    position_id="12345",
    uic=42,
    amount=10000,
    asset_type="FxSpot",
    buy_sell="Sell",
)
result = client.validate_order(spec)
print(result.get("PreCheckResult"))
```

## IsForceOpen

- **Stock**: API 非対応のため、`SaxoClient` が送信前に自動除去します。
- **CFD / FX**: `IsForceOpen=True` で両建て可能です。決済は `close_force_open_*`。

## 関連

- [option_trader.md](option_trader.md) — オプション取引用 Layer 3
- [orders.md](orders.md) — Layer 2 注文ビルダー（PositionOpen / PositionClose）
