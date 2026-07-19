# saxo-api-client (AI-Ready)

English | [日本語](./README.ja.md)

> Canonical README (English). The Japanese file is a translation of this document.

---

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![AI-First](https://img.shields.io/badge/AI--First-Optimized-success.svg)
![Type Safety](https://img.shields.io/badge/Type%20Safety-Strictly%20Typed-blue.svg)
![Docs](https://img.shields.io/badge/Docs-AI--Ready-orange.svg)

A modern client library designed to access Saxo Bank OpenAPI from Python, featuring **optimizations for AI assistants (AI-First)** to ensure efficiency and safety.

This library is a fork and re-architected version of the original [hootnot/saxo_openapi](https://github.com/hootnot/saxo_openapi) optimized for modern AI-assisted development workflows. **Today's advancement is built on the extensive initial efforts and implementations of the original author, hootnot.**

---

## 💎 Key Features: AI-First Documentation

The defining feature of this library is its design, which allows AI assistants (Claude, GPT-4, Gemini, etc.) to retrieve accurate information and support developers with minimal token consumption.

1. **Separation of Documentation**: Detailed docstrings have been offloaded from the Python code to external Markdown files (`docs/api/`). AI assistants only read documentation when necessary, conserving context window space.
2. **AI Navigation Map (`.ai/index.json`)**: All endpoints, categories, and use cases are indexed in structured JSON metadata. AI assistants can find target endpoints instantly.
3. **Rich Examples and Schemas**: Includes over 275 JSON Schemas (`docs/schemas/`) and ready-to-run workflow examples (`docs/examples/`).
4. **Strict Typing (Python 3.13+)**: Designed for static analysis using tools like `mypy` to prevent runtime bugs before they happen.
5. **Dynamic Rate Limit Handling**: Automatically detects HTTP 429 rate limit errors from the API, dynamically parses the rate limit reset time, waits, and retries.
6. **Robust Authentication Support**: Fully integrated OAuth 2.0 authentication and session management. No external libraries required.

---

## 📚 Documentation Portal

Please refer to the guides inside the `docs/` directory for detailed information:

- **[Master Index (docs/README.md)](docs/README.md)** - Entry point to all documentation.
- **[Quick Start Guide (docs/quickstart.md)](docs/quickstart.md)** - Run your first request in 5 minutes.
- **[Authentication Guide (docs/authentication.md)](docs/authentication.md)** - Connection configuration and token lifecycle.
- **[AI-First Migration Guide (docs/MIGRATION.md)](docs/MIGRATION.md)** - Key differences from the legacy library architecture.

---

## 🚀 Quick Start

### Installation

**Recommended (PyPI)** — works with both pip and uv:

```bash
pip install saxo-api-client
# or
uv add saxo-api-client
```

**Optional (GitHub tip / unreleased commits):**

```bash
pip install git+https://github.com/nohikomiso/saxo-api-client.git
# or
uv add git+https://github.com/nohikomiso/saxo-api-client.git
```

### For AI agents (any tool)

Do **not** invent per-IDE skills that duplicate trading rules. One canonical guide ships **inside the installed package**:

```bash
saxo-api-client agent-guide
# or
python -m saxo_api_client.agent
# optional: write a copy next to your project
saxo-api-client agent-guide -o ./AGENTS_SAXO.md
```

Python:

```python
from saxo_api_client.agent import read_guide
print(read_guide())
```

That guide is the source of truth for Layer 3 (`SaxoClient` / `OptionTrader`), pitfalls, and removed `SaxoTrader`. Tool-specific skill files should only **point** at it.

For **endpoint / schema lookup** (not trading), prefer the PyPI MCP [`mcp-server-saxo-openapi`](https://pypi.org/project/mcp-server-saxo-openapi/) — see [Related Resources](#-related-resources).

### Your First Request (Using SaxoClient Facade)

The `SaxoClient` is the unified facade class that provides an intuitive, one-liner interface for all common trading operations, completely hiding the complex underlying endpoints.

```python
import json
from saxo_api_client.contrib.client import SaxoClient
from saxo_api_client.auth import SaxoAuthClient
from saxo_api_client import AssetType, OrderType

# Optional: Define a callback to securely save the token when it refreshes
def save_token(token_data):
    with open("token.json", "w") as f:
        json.dump(token_data.model_dump(), f)

# 1. Initialize the Auth Client and login
auth = SaxoAuthClient(app_config="app_config.json", on_token_refresh=save_token)
auth.login(launch_browser=True, catch_redirect=True)

# 2. Initialize the ultimate facade client
client = SaxoClient(auth_client=auth)

# Check account balance with a single line
balance = client.get_account_balance()
print("Balance:", balance)

# Safely check if the market is open and the order is accepted
if client.is_order_accepted(symbol="AAPL", asset_type=AssetType.CfdOnStock, order_type=OrderType.Market):
    # Place a market order without worrying about Uic resolution
    response = client.market_order(
        symbol="AAPL",
        amount=10,
        asset_type=AssetType.CfdOnStock
    )
    print("Order placed:", response)
else:
    print("Market is closed or order type not accepted.")
```

### API Request/Response Tracing (For Research and Debugging)

When researching new features or API behaviors, you can configure the client to record request and response pairs as local JSON files (usually disabled in production).

```bash
export SAXO_OPENAPI_TRACE=1
export SAXO_OPENAPI_TRACE_DIR=api_traces
uv run python your_research_script.py
```

```python
from saxo_api_client import API

client = API(access_token=token, trace_dir="api_traces")  # Can also be enabled via parameter
```

- Save path: `api_traces/{YYYYMMDD}/saxo_{endpoint}_{trace_id}.json` (add to gitignore).
- Verified responses can be manually promoted to the `response/` folder of this repo.
- Sensitive information like tokens and `AccountKey` are automatically masked.

## 🏛 The 3-Tier Architecture

To shield developers from the complexity of Saxo Bank's APIs (such as mandatory `AccountKey` injection and resolving Tickers to numeric `Uic`s), this library provides a robust 3-Tier Architecture.

- **Layer 3 (High-Level API - Recommended)**: `SaxoClient`, `OptionTrader`
  - Primary facade for trading. Prefer `SaxoClient` for FX / Stock / CFD (`market_order`, `limit_order`, `stop_order`, …) and `OptionTrader` for options.
  - Resolves tickers (Symbol) to `Uic` (including `PrimaryListing` fallback when multiple hits occur).
  - Injects `AccountKey` and builds nested order parameters. (`SaxoTrader` was removed; do not import it.)
- **Layer 2 (Order Builders)**: `MarketOrder`, `LimitOrder`, `StopOrder`, etc.
  - Used for advanced customization when Layer 3 does not cover an edge case (or with `SaxoClient.validate_order` / `place_order`).
- **Layer 1 (OpenAPI FlexModels)**: Pydantic `_FlexModel` (`TradeOrdersRequest`, etc.)
  - Schema validation before requests are sent. Developers rarely interact with this layer directly.
- **Layer 0 (Transport)**: `API`, `SaxoAuthClient`, `endpoints.*`
  - Raw HTTP / OAuth Command-pattern clients.

---

## 🛠 Recommended Architecture

To maximize the benefits of this library and run 24/7 stable algorithmic trading, we recommend the following "Separation of Concerns" multi-service configuration.

### 1. Separation of Auth and Trading Operations
Run the authentication manager and the trading/data execution logic in separate, independent processes.

- **Auth Service (using `saxo_api_client.auth.SaxoAuthClient`)**: Handles OAuth logins, keeps the session alive, and writes the latest token to a local file (e.g., `saxo_token.json`).
- **Trading Services (using saxo-api-client)**: Simply reads the saved token file to execute commands like balance retrieval, price monitoring, or orders without needing to handle the OAuth flow directly.

### 2. Advantages
- **Robustness**: If an authentication issue occurs, the Auth Service handles recovery without needing to restart the active trading loops.
- **Scalability**: Multiple independent micro-services (e.g., market monitor, execution engine, notifier) can run concurrently by referencing the single token file.

---

## ⚠️ Disclaimer: Streaming Features

The streaming features in this library (Saxo-OpenAPI) are currently under active development and considered incomplete.

- **Supported Scope**: Basic connectivity establishment and resource subscription registration are tested and work.
- **Missing Features**: Message decoding efficiency, dynamic reconnection handling, parallel processing safety, and performance optimization are not yet implemented.
- **Recommendation**: For production real-time trading or heavy data ingestion, **do not rely on the built-in streaming features; implement your own robust stream handling instead.**

---

## 📂 Directory Structure

- `saxo_api_client/`: Core library source code. Compact docstrings optimized for AI tools.
- `docs/api/`: **[Main]** Japanese documentation for all endpoints.
- `docs/schemas/`: Over 270 JSON Schemas representing requests and responses.
- `docs/examples/`: Practical workflow examples (balance check, order execution, streaming, etc.).
- `saxo_api_client/contrib/`: High-level facades (`SaxoClient`, `OptionTrader`) and order builders.
- `samples/`: **[New]** Example scripts to verify operations in real/SIM environments (FX, options, order lifecycles).
- `tests/`: Unit and integration tests for the library.
- `.ai/`: Structured index and metrics metadata for AI assistants.

---

## 🧪 Testing & Verification

The `samples/` directory contains various scripts simulating actual trading workflows:
- `verify_lifecycle_trading.py`: Confirms the entire lifecycle of an order from submission to execution.
- `verify_refdata_fx.py`: Fetches reference data for FX currency pairs.
- `verify_portfolio_fx.py`: Checks portfolio balance and position configurations.

These serve as excellent reference material for utilizing the library.

You can also run unit tests with:
```bash
pytest tests/
```

---

## 🔗 Related Resources

### For AI agents (preferred)

Use the **OpenAPI lookup MCP** (offline reference; does **not** trade). Spec source lives in the `mcp-server-saxo-openapi` project (PyPI: [`mcp-server-saxo-openapi`](https://pypi.org/project/mcp-server-saxo-openapi/)).

```json
{
  "mcpServers": {
    "saxo-openapi": {
      "command": "uvx",
      "args": ["mcp-server-saxo-openapi"]
    }
  }
}
```

CLI fallback:

```bash
uvx --from mcp-server-saxo-openapi saxo-doc-helper search-endpoints orders
```

Together with this package’s agent guide (`saxo-api-client agent-guide`): MCP = endpoint/schema facts + pitfalls; `SaxoClient` GUIDE = how to call this library.

### For humans

- **[SaxoBank OpenAPI Docs (Markdown)](https://github.com/nohikomiso/SaxoBank-OpenAPI-Docs)** — readable community Markdown of Saxo docs (browsing / deep reading).
- **[Official Saxo OpenAPI](https://www.developer.saxo/openapi/referencedocs)** — vendor reference.
- This repo’s `docs/` (when cloning) — library-oriented guides and examples.

---

## 🙏 Acknowledgments

The core codebase of this project and the foundation of wrapping Saxo OpenAPI in Python were passionately developed by **[hootnot (GitHub)](https://github.com/hootnot)**.

The design principles established by him over years of maintenance allowed us to evolve this library into a modern "AI-First" tool. **Regardless of current maintenance status, we express our highest respect and gratitude for his pioneering work.**

## ⚖️ License

MIT License (inherited from the original repository). See `LICENSE` for details.
