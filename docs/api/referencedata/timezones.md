# ReferenceData - Time Zones

> **パラメータ詳細は MCP へ**: `mcp-server-saxo-openapi`（`get_saxo_endpoint_spec` / `saxo-doc-helper`）。このファイルは **Python バインディング索引**です。

Saxo Bank がサポートするタイムゾーンのリストを取得します。

## エンドポイント

### TimeZones - タイムゾーン一覧取得

Saxo Bank でサポートされているすべてのタイムゾーンのリストを取得します。

**エンドポイント:** `GET /openapi/ref/v1/timezones/`

**パラメータ:** なし

**レスポンス:**
- JSON Schema: [time_zones_response.json](../../schemas/referencedata/timezones/time_zones_response.json)

**使用例:**

```python
import json
import saxo_api_client
import saxo_api_client.endpoints.referencedata as rd

client = saxo_api_client.API(access_token=...)

# サポートされているタイムゾーンの一覧を取得
r = rd.timezones.TimeZones()
client.request(r)
print(json.dumps(r.response, indent=2))
```

**レスポンス例:**

```json
{
  "Data": [
    {
      "TimeZoneId": 1,
      "Name": "UTC",
      "Offset": "+00:00"
    },
    {
      "TimeZoneId": 2,
      "Name": "Eastern Standard Time",
      "Offset": "-05:00"
    },
    {
      "TimeZoneId": 3,
      "Name": "Tokyo Standard Time",
      "Offset": "+09:00"
    }
  ]
}
```

---

## 主要フィールド

- `TimeZoneId`: タイムゾーンID
- `Name`: タイムゾーン名
- `Offset`: UTCからのオフセット

## ユースケース

- 取引時間の表示
- 市場時間の変換
- ユーザー設定のタイムゾーン選択

## 関連エンドポイント

- [Exchanges](./exchanges.md) - 取引所参照データ
- [Cultures](./cultures.md) - カルチャー参照データ

## 参考リンク

- [Saxo Bank OpenAPI リファレンス](https://www.developer.saxo/)
- [IANA Time Zone Database](https://www.iana.org/time-zones)
