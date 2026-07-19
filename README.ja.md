# saxo-api-client (AI-Ready)

[English](./README.md) | 日本語

> 正本は [README.md](./README.md)（英語）です。本ファイルはその日本語訳です。

---

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![AI-First](https://img.shields.io/badge/AI--First-Optimized-success.svg)
![Type Safety](https://img.shields.io/badge/Type%20Safety-Strictly%20Typed-blue.svg)
![Docs](https://img.shields.io/badge/Docs-AI--Ready-orange.svg)

Saxo Bank OpenAPI を Python から効率的かつ安全に利用するための、**AI アシスタント向け最適化（AI-First）** を備えた現代的なクライアントライブラリです。

本ライブラリは、オリジナルの [hootnot/saxo_openapi](https://github.com/hootnot/saxo_openapi) をベースに、AI 支援開発フロー向けに再設計したフォークです。**今日の発展は、原作者 hootnot 氏による初期の多大な努力と実装の上に成り立っています。**

---

## 💎 主な特徴: AI-First Documentation

本ライブラリの最大の特徴は、AI アシスタント（Claude, GPT-4, Gemini 等）が最小限のトークン消費で正確な情報を取得し、開発を支援できるように設計されている点です。

1. **ドキュメントの分離**: 詳細な docstring を Python コードから外部 Markdown（`docs/api/`）へ移管。AI は必要なときだけドキュメントを読むため、コンテキストを節約できます。
2. **AI ナビゲーションマップ（`.ai/index.json`）**: 全エンドポイント・カテゴリ・ユースケースを構造化 JSON で索引化。目的のエンドポイントを瞬時に探せます。
3. **豊富な実行例とスキーマ**: 275 個超の JSON Schema（`docs/schemas/`）と、すぐ動かせるワークフロー例（`docs/examples/`）を同梱。
4. **厳格な型定義（Python 3.13+）**: `mypy` 等の静的解析を前提とし、実行前にバグを防ぎます。
5. **動的レート制限処理**: API の HTTP 429 を検知し、リセット時刻を解析して待機・リトライします。
6. **堅牢な認証サポート**: OAuth 2.0 認証とセッション管理を内蔵。外部ライブラリ不要です。

---

## 📚 ドキュメントポータル

詳細は `docs/` 内の各ガイドを参照してください。

- **[総合インデックス (docs/README.md)](docs/README.md)** — ドキュメント全体の入り口
- **[クイックスタート (docs/quickstart.md)](docs/quickstart.md)** — 5 分で最初のリクエスト
- **[認証ガイド (docs/authentication.md)](docs/authentication.md)** — 接続設定とトークンライフサイクル
- **[AI-First 移行ガイド (docs/MIGRATION.md)](docs/MIGRATION.md)** — 旧アーキテクチャとの主な差分

---

## 🚀 クイックスタート

### インストール

**推奨（PyPI）** — pip / uv どちらでも可:

```bash
pip install saxo-api-client
# または
uv add saxo-api-client
```

**任意（GitHub tip / 未リリースコミット）:**

```bash
pip install git+https://github.com/nohikomiso/saxo-api-client.git
# または
uv add git+https://github.com/nohikomiso/saxo-api-client.git
```

### AI エージェント向け（ツール非依存）

IDE ごとにスキルを複製しないでください。取引ルールの正本は **インストール済みパッケージ内** のガイド 1 本です。

```bash
saxo-api-client agent-guide
# または
python -m saxo_api_client.agent
# 任意: プロジェクトへコピー
saxo-api-client agent-guide -o ./AGENTS_SAXO.md
```

Python:

```python
from saxo_api_client.agent import read_guide
print(read_guide())
```

Layer 3（`SaxoClient` / `OptionTrader`）、落とし穴、削除済み `SaxoTrader` の正本はここにあります。ツール固有スキルは **このガイドを指すだけ** にしてください。

### 最初のリクエスト（SaxoClient ファサード）

`SaxoClient` は共通の取引操作をワンライナーで提供する統合ファサードで、複雑なエンドポイント層を隠蔽します。

```python
import json
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.auth import SaxoAuthClient
from saxo_api_client import AssetType, OrderType

# オプション: トークン更新時に安全に保存するコールバック
def save_token(token_data):
    with open("token.json", "w") as f:
        json.dump(token_data.model_dump(), f)

# 1. 認証クライアントの初期化とログイン
auth = SaxoAuthClient(app_config="app_config.json", on_token_refresh=save_token)
auth.login(launch_browser=True, catch_redirect=True)

# 2. ファサードクライアントの初期化
client = SaxoClient(auth_client=auth)

# 口座残高を 1 行で取得
balance = client.get_account_balance()
print("Balance:", balance)

# 市場が開き、注文が受け付けられるか確認してから成行
if client.is_order_accepted(symbol="AAPL", asset_type=AssetType.CfdOnStock, order_type=OrderType.Market):
    # UIC 解決を気にせず成行注文
    response = client.market_order(
        symbol="AAPL",
        amount=10,
        asset_type=AssetType.CfdOnStock
    )
    print("Order placed:", response)
else:
    print("Market is closed or order type not accepted.")
```

### API 送受信トレース（調査・デバッグ用）

新機能や API 挙動の調査時は、リクエスト／レスポンスのペアをローカル JSON に記録できます（本番では通常 OFF）。

```bash
export SAXO_OPENAPI_TRACE=1
export SAXO_OPENAPI_TRACE_DIR=api_traces
uv run python your_research_script.py
```

```python
from saxo_api_client import API

client = API(access_token=token, trace_dir="api_traces")  # 引数でも有効化可
```

- 保存先: `api_traces/{YYYYMMDD}/saxo_{endpoint}_{trace_id}.json`（gitignore 推奨）
- 確定した応答は、このリポジトリの `response/` へ手動で昇格できます
- トークンや `AccountKey` などの機密情報は自動マスクされます

## 🏛 3 層アーキテクチャ

Saxo Bank API 特有の複雑さ（必須の `AccountKey` 注入、ティッカーから数値 `Uic` への解決など）から開発者を守るため、本ライブラリは次の 3 層（＋ Transport）構成です。

- **Layer 3（高レベル API・推奨）**: `SaxoClient`, `OptionTrader`
  - 取引の主入口。FX / Stock / CFD は `SaxoClient`（`market_order`, `limit_order`, `stop_order` など）、オプションは `OptionTrader` を使う
  - ティッカー（Symbol）を `Uic` に解決（複数ヒット時は `PrimaryListing` フォールバック）
  - `AccountKey` を注入し、ネストした注文パラメータを構築する（旧 `SaxoTrader` は削除済み。import しないこと）
- **Layer 2（注文ビルダー）**: `MarketOrder`, `LimitOrder`, `StopOrder` など
  - Layer 3 で足りない特殊ケース向け（または `SaxoClient.validate_order` / `place_order` と併用）
- **Layer 1（OpenAPI FlexModels）**: Pydantic `_FlexModel`（`TradeOrdersRequest` など）
  - 送信前のスキーマ検証。通常は直接触らない
- **Layer 0（Transport）**: `API`, `SaxoAuthClient`, `endpoints.*`
  - 生の HTTP / OAuth、Command パターンのクライアント

---

## 🛠 推奨システム構成

本ライブラリを活かし、24/7 のアルゴ取引を安定運用するには、関心責務分離のマルチサービス構成を推奨します。

### 1. 認証と取引操作の分離
認証管理と、取引／データ取得ロジックを別プロセスで動かします。

- **認証サービス（`saxo_api_client.auth.SaxoAuthClient`）**: OAuth ログイン、セッション維持、最新トークンのローカルファイル書き出し（例: `saxo_token.json`）
- **取引サービス（saxo-api-client）**: 保存済みトークンを読むだけで、残高取得・価格監視・注文などを実行（OAuth フロー不要）

### 2. 利点
- **堅牢性**: 認証障害があっても、取引ループを再起動せず認証サービス側で復旧できる
- **拡張性**: 同一トークンファイルを参照する監視・執行・通知など、複数マイクロサービスを並行稼働しやすい

---

## ⚠️ 注意: ストリーミング機能

本ライブラリのストリーミング機能は開発途上で、未完成とみなしてください。

- **対応範囲**: 接続確立と購読登録は動作確認済み
- **未実装**: 受信デコード効率、動的再接続、並列安全性、性能最適化など
- **推奨**: 本番のリアルタイム取引や大量データ取得では、**内蔵ストリーミングに頼らず独自の受信実装を使うこと**

---

## 📂 ディレクトリ構成

- `saxo_api_client/`: コア実装。AI 向けにコンパクトな docstring
- `docs/api/`: **[メイン]** 全エンドポイントの日本語ドキュメント
- `docs/schemas/`: リクエスト／レスポンス用 JSON Schema（270 超）
- `docs/examples/`: 実践的ワークフロー例（残高、注文、ストリーミングなど）
- `saxo_api_client/contrib/`: 高レベルファサード（`SaxoClient`, `OptionTrader`）と注文ビルダー
- `samples/`: **[New]** 実環境／SIM での検証スクリプト（FX、オプション、注文ライフサイクルなど）
- `tests/`: ライブラリの単体・結合テスト
- `.ai/`: AI アシスタント用の構造化インデックスとメトリクス

---

## 🧪 検証とテスト

`samples/` には実際の取引フローを模したスクリプトがあります。

- `verify_lifecycle_trading.py`: 発注から約定までのライフサイクル確認
- `verify_refdata_fx.py`: FX 通貨ペアの参照データ取得
- `verify_portfolio_fx.py`: ポートフォリオ残高・ポジション確認

ライブラリ利用時の優れた参照になります。

単体テスト:

```bash
pytest tests/
```

---

## 🔗 関連リソース

- **[SaxoBank OpenAPI Docs（Markdown 版）](https://github.com/nohikomiso/SaxoBank-OpenAPI-Docs)**: Saxo 公式開発者ドキュメントのコミュニティ維持 Markdown 版

---

## 🙏 謝辞

本プロジェクトのコアコードベースと、Saxo OpenAPI を Python で扱う基盤は、**[hootnot (GitHub)](https://github.com/hootnot)** 氏が情熱をもって開発したものです。

長年のメンテナンスで確立された設計思想のおかげで、本ライブラリを現代的な「AI-First」ツールへ進化させることができました。**現在のメンテナンス状況にかかわらず、先駆的な貢献に最大の敬意と感謝を表します。**

## ⚖️ ライセンス

MIT License（オリジナルリポジトリを継承）。詳細は `LICENSE` を参照してください。
