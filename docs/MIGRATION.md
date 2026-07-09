# saxo_api_client AI-First Migration Guide

## Overview

本ドキュメントは、saxo_api_client ライブラリのAI-First Documentation Refactoringにおける移行プロセスを説明します。

## 旧アーキテクチャ: @dyndoc_insert システム

### 概要
- **期間**: ~2025-11-21（Phase 6完了まで）
- **コンセプト**: 動的ドキュメント生成によるDRY原則の実現
- **問題点**: プレースホルダー未展開、AI効率の低さ、メンテナンス困難

### 技術詳細

#### @dyndoc_insert デコレータ

**実装場所**: `saxo_api_client/endpoints/decorators.py:6-58`

**動作原理**:
```python
@dyndoc_insert(responses)
class AccountDetails(endpoints.AccountDetails):
    """
    Get account details.

    Output::
        {_v3_AccountDetails_resp}  # ← import時に展開
    """
    pass
```

1. クラスimport時にデコレータが実行
2. docstring内のプレースホルダー（`{_v3_XXX_YYY}`）を正規表現で抽出
3. responses/*.py から対応するデータを取得
4. JSON整形（indent=2, 16文字インデント）して置換

#### プレースホルダー規約

| パターン | 対応データ | 用途 | 数量 |
|---------|----------|------|------|
| `{_v3_XXX_params}` | `responses['_v3_XXX']['params']` | GETクエリパラメータ | 52個 |
| `{_v3_XXX_resp}` | `responses['_v3_XXX']['response']` | レスポンスボディ | 55個 |
| `{_v3_XXX_body}` | `responses['_v3_XXX']['body']` | POST/PATCHボディ | 33個 |
| `{_v3_XXX_url}` | `responses['_v3_XXX']['url']` | エンドポイントURL | 50個 |
| 合計 | - | - | **190個** |

#### responsesデータ構造

**配置**: `saxo_api_client/endpoints/*/responses/*.py` (37ファイル、8,002行)

**構造**:
```python
responses = {
    "_v3_AccountDetails": {
        "url": "/openapi/port/v1/accounts/{AccountKey}",
        "response": {
            "CreationDate": "2025-02-02T10:47:42.313000Z",
            "AccountType": "Normal",
            ...
        }
    },
    "_v3_Order": {
        "url": "/openapi/trade/v2/orders",
        "body": {
            "AccountKey": "Cf4xZWiYL6W1nMKpygBLLA==",
            "Amount": "10000",
            ...
        },
        "response": {
            "OrderId": "76288494"
        }
    },
    ...
}
```

**フィールド**:
- `url` (str, required): エンドポイントURL
- `params` (dict, optional): クエリパラメータ例（GETリクエスト）
- `body` (dict, optional): リクエストボディ例（POST/PATCH/PUT）
- `response` (dict/list, required): レスポンス例

### 問題点の詳細

1. **プレースホルダー未展開**:
   - @dyndoc_insertがimport時のみ実行されるため、ソースコード上は未展開
   - 静的解析ツール、IDEでは未展開のまま表示
   - AIアシスタントがソースコードを読む際、プレースホルダーのまま

2. **AI効率の低さ**:
   - 全docstringが展開されるため、1ファイルあたり数千行に膨張
   - トークン消費量が膨大（1クエリで数万トークン）
   - 必要な情報へのアクセスが困難

3. **メンテナンス困難**:
   - ドキュメント更新時、Pythonコードとresponsesファイルの両方を編集
   - responses/*.py の更新が反映されない場合がある（キャッシュ問題）
   - バグの温床（21件のバグが発見された）

## 新アーキテクチャ: AI-First Documentation

### 概要
- **開始**: 2025-11-21（Phase 1）
- **コンセプト**: ドキュメント完全分離によるAI効率化とバグ削減
- **目標**: コード60-70%削減、AIトークン50%削減

### 設計原則

1. **Single Responsibility**: コードは実装のみ、ドキュメントは説明のみ
2. **外部化**: 全ドキュメント・例・スキーマを外部管理（Markdown + JSON）
3. **構造化メタデータ**: `.ai/index.json` でAIナビゲーション
4. **段階的移行**: Phase 1-6 で影響範囲を制御

### 新ディレクトリ構造

```
libs/ (monorepo root)
├── saxo_api_client/ (this repository root)
│   ├── endpoints/
│   │   ├── portfolio/
│   │   │   ├── balances.py          # 最小限docstring（1行+リンク）
│   │   │   ├── positions.py
│   │   │   └── ...
│   │   └── ...
│   └── ...
├── docs/
│   ├── api/
│   │   ├── portfolio/
│   │   │   ├── balances.md          # 完全なドキュメント（日本語）
│   │   │   ├── positions.md
│   │   │   └── ...
│   │   └── ...
│   ├── schemas/
│   │   ├── portfolio/
│   │   │   ├── balances/
│   │   │   │   ├── account_balances_me_response.json
│   │   │   │   ├── account_balances_me_params.json (if exists)
│   │   │   │   └── ...
│   │   │   └── ...
│   │   └── ...
│   ├── contrib/
│   │   ├── orders.md
│   │   ├── websocket.md
│   │   └── ...
│   └── examples/
│       ├── check_balance.md
│       ├── place_market_order.md
│       └── ...
└── .ai/
    └── index.json                   # AIナビゲーションメタデータ
```

### 移行マッピング

#### Before (旧アーキテクチャ)
```python
# saxo_api_client/endpoints/portfolio/balances.py
from .responses.balances import responses

@dyndoc_insert(responses)
class AccountBalancesMe(endpoints.AccountBalancesMe):
    """
    Get balance for logged-in client.

    Output::
        {_v3_AccountBalancesMe_resp}  # 数百行のJSON
    """
    ENDPOINT = "openapi/port/v1/balances/me"
    METHOD = "GET"
```

#### After (新アーキテクチャ)
```python
# saxo_api_client/endpoints/portfolio/balances.py
class AccountBalancesMe(endpoints.AccountBalancesMe):
    """Get balance for logged-in client. See docs/api/portfolio/balances.md#accountbalancesme"""
    ENDPOINT = "openapi/port/v1/balances/me"
    METHOD = "GET"
```

```markdown
<!-- docs/api/portfolio/balances.md -->
# Portfolio - Balances

## AccountBalancesMe

### APIリファレンスとスキーマ定義の活用

AIアシスタントは、必要に応じて以下のファイルを参照し、正確なパラメータや型情報を取得します。

- **`docs/api/`**: エンドポイントごとの詳細なMarkdownドキュメント
- **`docs/schemas/`**: Pydanticベースの正確なJSON Schema（自動生成済み）

---

## 認証基盤の統合 (No More Saxo-APY)

旧環境では、OAuth 2.0 認証を行うために外部の `Saxo-APY` リポジトリを利用することが推奨されていました。
しかし、本バージョンのアーキテクチャ改修により、**OAuth 2.0 クライアント（ローカルリダイレクトサーバーを含む）が完全に `saxo_api_client` 内部に統合されました**。

今後は `Saxo-APY` 等の外部パッケージは一切不要となります。
詳細は [認証ガイド(authentication.md)](authentication.md) を参照してください。

---

## 新アーキテクチャ: 3-Tier ArchitectureとPydantic FlexModel

今回の AI-First 移行において、ドキュメントの分離だけでなく、**「SaxoBank API 特有の複雑さ（Uic解決、AccountKey注入など）」を完全に隠蔽する3層アーキテクチャ** が確立されました。

### 1. Layer 3 (High-Level API - 推奨)
- **代表クラス**: `SaxoTrader`, `OptionTrader` (`saxo_api_client.contrib.trader` など)
- **役割**: 人間（およびAIアシスタント）が最も直感的に使える最上位APIです。
- **特徴**:
  - `market_order(Symbol="AAPL", AssetType="Stock")` のように、**ティッカーシンボル**での注文が可能です。
  - 裏側で `PrimaryListing` を用いた安全なUIC自動解決ロジックが走り、Saxo特有の「複数取引所ヒット問題」を自動回避します。
  - `AccountKey` の自動注入や、複雑なオーダー辞書の構築をすべて隠蔽します。

### 2. Layer 2 (Order Builders)
- **代表クラス**: `MarketOrder`, `LimitOrder`, `StopOrder` (`saxo_api_client.contrib.orders` など)
- **役割**: Layer 3 の内部で使われるか、あるいは Layer 3 では対応しきれない特殊な条件の注文を構築するための中級者向けヘルパー群です。
- **特徴**:
  - 手動でパラメータを組み立てたい場合や、特定のアルゴリズムトレードで細かい制御が必要な場合に使用します。

### 3. Layer 1 (OpenAPI FlexModels)
- **代表クラス**: `TradeOrdersRequest` 等 (`saxo_api_client.models` 法下の自動生成 Pydantic モデル)
- **役割**: API送信直前に自動介入して、Saxoの厳格なJSONスキーマに基づくバリデーションとシリアライズを行うインフラストラクチャ層です。
- **特徴**:
  - すべてのモデルは `_FlexModel` (`extra='allow'`) を継承しており、Saxo側での将来のAPI変更（新フィールド追加など）でクラッシュしない堅牢な設計（AI-First Resilience）となっています。
  - 人間が直接インスタンス化して使うことはほぼありません。

この3層構造により、「**基本は Layer 3 (`SaxoTrader`) を使い、必要に応じて Layer 2/1 に降りる**」という明確なベストプラクティスが生まれました。

### パラメータ
なし

### レスポンス

**成功時 (200 OK)**:
\`\`\`json
{
  "CalculationReliability": "Ok",
  "CashBalance": 999956.74,
  ...
}
\`\`\`

**スキーマ**: [account_balances_me_response.json](schemas/portfolio/balances/account_balances_me_response.json)

### 使用例
\`\`\`python
import saxo_api_client
# ...
\`\`\`
```

### 変換プロセス

#### Phase 1: JSON Schema自動生成

**スクリプト**: `scripts/convert_responses_to_json.py`

**処理フロー**:
```python
# 1. responsesファイルを動的import
from saxo_api_client.endpoints.portfolio.responses.balances import responses

# 2. 各エントリを処理
for key, data in responses.items():
    # _v3_AccountBalancesMe → account_balances_me
    endpoint_name = convert_to_snake_case(key.replace("_v3_", ""))

    # response スキーマ生成（必須）
    if 'response' in data:
        output_path = f"docs/schemas/portfolio/balances/{endpoint_name}_response.json"
        write_json(output_path, data['response'])

    # params スキーマ生成（存在する場合のみ）
    if 'params' in data and data['params']:
        output_path = f"docs/schemas/portfolio/balances/{endpoint_name}_params.json"
        write_json(output_path, data['params'])

    # body スキーマ生成（存在する場合のみ）
    if 'body' in data and data['body']:
        output_path = f"docs/schemas/portfolio/balances/{endpoint_name}_body.json"
        write_json(output_path, data['body'])
```

**生成数**:
- response スキーマ: 約190個（全エンドポイント）
- params スキーマ: 約52個（GETパラメータを持つエンドポイント）
- body スキーマ: 約33個（POST/PATCHボディを持つエンドポイント）
- **合計: 約275個**

#### Phase 2-3: Markdownドキュメント作成

**手動作業** (AI支援):
- responses/*.py のデータを参考に、完全なMarkdownドキュメント作成
- 日本語で記述（コード例のコメント除く）
- params/body/response の3種類の例をすべて含める
- JSON Schemaへのリンクを追加

#### Phase 6: 旧コード削除

**削除対象**:
- `saxo_api_client/endpoints/decorators.py` (全体)
- `saxo_api_client/endpoints/*/responses/` (37ファイル、8,002行)
- 全エンドポイントファイルの `@dyndoc_insert` デコレータ（89箇所）
- 全プレースホルダー（190個）

## 成功指標

| 指標 | 目標 | 測定方法 |
|------|------|---------|
| コードサイズ削減 | 60-70% | Phase 2の5ファイルで before/after 比較 |
| AIトークン削減 | 50%以下 | 同一クエリで token数比較 |
| エンドポイント発見速度 | 3ツール呼び出し以内 | .ai/index.json 使用時の測定 |
| ドキュメント数 | 48個以上 | find docs -name '*.md' \| wc -l |
| JSON Schema数 | 275個 | find docs/schemas -name '*.json' \| wc -l |

## トラブルシューティング

### Q1: プレースホルダーが未展開のまま残っている

**原因**: @dyndoc_insert がimport時のみ実行されるため、ソースコード上は未展開

**対処**: これは仕様です。実際にimportすると展開されます。
```python
from saxo_api_client.endpoints.portfolio.balances import AccountBalancesMe
print(AccountBalancesMe.__doc__)  # ← ここで展開済みのdocstringが表示される
```

### Q2: responses/*.py のデータが古い

**原因**: 実際のAPI仕様変更がresponsesファイルに反映されていない

**対処**: Phase 1-6 完了後は、Markdownドキュメントを直接更新してください。

### Q3: 変換スクリプトがエラーを出す

**確認事項**:
- Python 3.8以上を使用しているか
- saxo_api_client がインストールされているか（例: `pip install git+https://github.com/nohikomiso/saxo-api-client.git`）
- responsesファイルがすべて存在するか

## 参考資料

- 要件定義: `.kiro/specs/saxo-api-client-refactoring/requirements.md`
- 技術設計: `.kiro/specs/saxo-api-client-refactoring/design.md`
- タスク一覧: `.kiro/specs/saxo-api-client-refactoring/tasks.md`
- AI Navigation: `.ai/index.json`
