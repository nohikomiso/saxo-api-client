# Portfolio Positions

> **パラメータ詳細は MCP へ**: `GET /port/v1/positions/...`。
> ForceOpen 決済の `PositionId` は **PositionsQuery レスポンスのトップレベル**（`SaxoClient.iter_open_positions`）。
> このファイルは Python バインディング索引です。

`saxo_api_client.endpoints.portfolio.positions`

| クラス | Method | Path |
|--------|--------|------|
| `SinglePosition` | GET | `/port/v1/positions/{PositionId}` |
| `SinglePositionDetails` | GET | `/port/v1/positions/{PositionId}/details` |
| `PositionsMe` | GET | `/port/v1/positions/me` |
| `PositionsQuery` | GET | `/port/v1/positions` |
| `PositionListSubscription` | POST | subscription |
| `PositionSubscriptionPageSize` | PUT | subscription page size |
| `PositionSubscriptionRemoveMultiple` | DELETE | remove multiple |
| `PositionSubscriptionRemove` | DELETE | remove one |

## 最小例

```python
import saxo_api_client.endpoints.portfolio as pf
from saxo_api_client.contrib.client import SaxoClient

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")
# 推奨: PositionId 正規化済み
for row in client.iter_open_positions(uic=42):
    print(row["position_id"], row["is_force_open"], row["amount"])

# 低レベル
api = client._api
r = pf.positions.PositionsQuery(params={"ClientKey": "...", "AccountKey": client.account_key})
api.request(r)
```

決済手順: [close_position.md](../../examples/close_position.md)

## スキーマ

[schemas/portfolio/positions/](../../schemas/portfolio/positions/)
