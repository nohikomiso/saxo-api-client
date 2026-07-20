# Trading Positions

> **パラメータ詳細は MCP へ**: `get_saxo_endpoint_spec` / `saxo-doc-helper`。
> 通常の建玉取得・決済は Portfolio Positions + [close_position.md](../../examples/close_position.md)。
> このファイルは Python バインディング索引です。

`saxo_api_client.endpoints.trading.positions`

| クラス | Method | 用途 |
|--------|--------|------|
| `PositionByQuote` | POST | クォート受諾でポジション作成 |
| `UpdatePosition` | PATCH | ポジション更新（例: FX オプション ExerciseMethod） |
| `ExercisePosition` | PUT | 特定ポジションの行使 |
| `ExerciseAmount` | PUT | UIC 横断の行使 |

## 最小例

```python
import saxo_api_client.endpoints.trading as tr
from saxo_api_client import API

client = API(access_token="YOUR_ACCESS_TOKEN")
r = tr.positions.PositionByQuote(data={"QuoteId": "...", "Amount": 1000})
client.request(r)
```

## スキーマ

[schemas/trading/positions/](../../schemas/trading/positions/)
