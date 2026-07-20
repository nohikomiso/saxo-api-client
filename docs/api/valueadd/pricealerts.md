# Price Alerts Services

> **パラメータ詳細は MCP へ**。このファイルは Python バインディング索引です。

`saxo_api_client.endpoints.valueadd.pricealerts`

| クラス | 用途 |
|--------|------|
| `GetAllAlerts` | アラート定義一覧 |
| `GetAlertDefinition` | 単一アラート定義 |
| `CreatePriceAlert` | 作成 |
| `UpdatePriceAlert` | 更新 |
| `DeletePriceAlert` | 削除 |
| `GetUserNotificationSettings` | 通知設定取得 |
| `ModifyUserNotificationSettings` | 通知設定変更 |

## 最小例

```python
import saxo_api_client.endpoints.valueadd as va
from saxo_api_client import API

client = API(access_token="YOUR_ACCESS_TOKEN")
r = va.pricealerts.GetAllAlerts(params={"State": "Active"})
client.request(r)
```

## スキーマ

[schemas/valueadd/](../../schemas/valueadd/)（存在する場合）
