# Accounts

> **パラメータ詳細は MCP へ**。このファイルは Python バインディング索引です。

`saxo_api_client.endpoints.portfolio.accounts`

| クラス | 用途 |
|--------|------|
| `AccountDetails` | 単一口座詳細 |
| `AccountsMe` | ログインユーザーの口座一覧 |
| `AccountListByClient` | クライアント別口座一覧 |
| `AccountUpdate` | 口座更新 |
| `AccountReset` | 口座リセット |
| `SubscriptionCreate` | 口座サブスクリプション |
| `SubscriptionRemoveByTag` | タグで購読削除 |
| `SubscriptionRemoveById` | ID で購読削除 |

## 最小例

```python
from saxo_api_client.contrib.client import SaxoClient

client = SaxoClient(access_token="YOUR_ACCESS_TOKEN")
print(client.get_accounts())
```

## スキーマ

[schemas/portfolio/accounts/](../../schemas/portfolio/accounts/)
