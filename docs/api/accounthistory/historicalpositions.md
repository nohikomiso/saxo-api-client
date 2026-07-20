# accounthistory.historicalpositions

> **パラメータ詳細は MCP へ**: `mcp-server-saxo-openapi`（`get_saxo_endpoint_spec` / `saxo-doc-helper`）。このファイルは **Python バインディング索引**です。

`accounthistory` グループの `historicalpositions` モジュールです。

## HistoricalPositions

クライアントが所有する特定のアカウントの過去のポジションリストを取得します。
必須フィールドは `ClientKey` と、`StandardPeriod` または `FromDate`/`ToDate` のいずれかです。

`GET openapi/hist/v3/positions/{ClientKey}`

### パラメータ

| パラメータ | 型 | 必須 | 説明 |
|------------|------|------|------|
| ClientKey | string | Yes | クライアントキー |
| params | dict | Yes | クエリパラメータ（StandardPeriod または FromDate/ToDate が必須） |

### 使用例

```python
import saxo_api_client
import saxo_api_client.endpoints.accounthistory as ah
import json

client = saxo_api_client.API(access_token=...)
ClientKey = 'Cf4xZWiYL6W1nMKpygBLLA=='
params = {
    'FromDate': '2019-03-01',
    'ToDate': '2019-03-10'
}
r = ah.historicalpositions.HistoricalPositions(ClientKey=ClientKey,
                                               params=params)
client.request(r)
print(json.dumps(r.response, indent=2))
```

### レスポンス

成功時のレスポンススキーマは以下を参照してください:
[Response Schema](../../schemas/accounthistory/historicalpositions/historical_positions_response.json)
