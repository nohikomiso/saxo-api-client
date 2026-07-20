# デルタヘッジワークフロー例

オプションポジションのデルタを計算し、原資産（FX スポット）で**新規**ヘッジ注文を出す例です。
デルタ計算は簡略化されたダミーです。

決済（FIFO / ForceOpen）は [close_position.md](close_position.md) を参照。

## 前提条件

*   有効なアクセストークン
*   オプションポジションを保有していること

## コード例

```python
import json
from saxo_api_client import API
import saxo_api_client.endpoints.portfolio as pf
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.contrib.orders import PositionOpen
from saxo_api_client.contrib.session import account_info

token = "YOUR_ACCESS_TOKEN"
api = API(access_token=token)
client = SaxoClient(access_token=token)
ai = account_info(api)
print(f"AccountKey: {ai.AccountKey}")


def calculate_portfolio_delta(positions):
    total_delta = 0.0
    for pos in positions:
        if pos["NetPositionBase"]["AssetType"] == "FxVanillaOption":
            delta = 0.5  # ダミー
            amount = pos["NetPositionBase"]["Amount"]
            total_delta += delta * amount
    return total_delta


r = pf.netpositions.NetPositionsMe()
positions = api.request(r).get("Data", [])
current_delta = calculate_portfolio_delta(positions)
hedge_needed = 0 - current_delta
print(f"Current Portfolio Delta: {current_delta}")
print(f"Hedge Needed: {hedge_needed}")

THRESHOLD = 1000
if abs(hedge_needed) > THRESHOLD:
    buy_sell = "Buy" if hedge_needed > 0 else "Sell"
    order = PositionOpen.market(
        uic=21,
        amount=abs(hedge_needed),
        asset_type="FxSpot",
        buy_sell=buy_sell,
        is_force_open=False,  # ネット相殺ヘッジ。両建てで残すなら True
    )
    rv_order = client.place_order(order)
    print(f"Hedge order placed: {rv_order['OrderId']}")
else:
    print("No hedge needed (within threshold).")
```

## 解説

1. Observe → Orient → Decide → Act のループ例。
2. ヘッジは**新規／相殺の意図**を `is_force_open` で明示する。
3. ForceOpen 建玉を「閉じる」つもりで反対成行だけを出すと偽決済になる → [close_position.md](close_position.md)。
