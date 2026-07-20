# {モジュール名}

> **パラメータ詳細は MCP へ**: `mcp-server-saxo-openapi` の `get_saxo_endpoint_spec` / `saxo-doc-helper`。
> このファイルは **Python バインディング索引**（クラス名・path・最小例）です。

{モジュールの説明}

## エンドポイント

| クラス | Method | Path |
|--------|--------|------|
| `{EndpointClassName}` | `{method}` | `{url}` |

## 最小例

```python
import saxo_api_client
import saxo_api_client.endpoints.{category} as {category}

client = saxo_api_client.API(access_token="YOUR_ACCESS_TOKEN")
r = {category}.{subcategory}.{EndpointClassName}(...)
client.request(r)
```

## スキーマ（任意）

[schemas/](../../schemas/) 配下の JSON。通常の学習では MCP を優先。
