# saxo-api-client — Agent Guide (canonical)

**Audience:** any AI coding agent (Cursor, Claude, Codex, Windsurf, etc.).  
**Source of truth:** this file, shipped inside the installed package. Do not invent a parallel “SaxoTrader” layer.

```bash
# After: pip install saxo-api-client  OR  uv add saxo-api-client
saxo-api-client agent-guide
# or
python -m saxo_api_client.agent
```

Human docs: package README (English canonical) / README.ja.md (Japanese translation).  
Repo docs (clone only): `docs/contrib/client.md`, `docs/MIGRATION.md`.

---

## Entry points (use these)

| Goal | Use |
|------|-----|
| FX / Stock / CFD trading | `from saxo_api_client.contrib.client import SaxoClient` |
| Stock options / multileg | `from saxo_api_client.contrib.option_trader import OptionTrader` |
| Auth / OAuth | `from saxo_api_client.auth import SaxoAuthClient` |
| Raw REST | `from saxo_api_client import API` + `saxo_api_client.endpoints.*` |

**Removed:** `saxo_api_client.contrib.trader.SaxoTrader` — no shim. Always use `SaxoClient`.

---

## Architecture (do not flatten)

1. **Layer 3 — Facades (preferred):** `SaxoClient`, `OptionTrader`  
   AccountKey injection, Symbol→Uic resolution, order one-liners, `validate_order` (precheck).
2. **Layer 2 — Order builders:** `MarketOrder`, `LimitOrder`, `StopOrder`, `StopLimitOrder`, …  
   Build bodies; pass to `SaxoClient.validate_order` / `place_order`.
3. **Layer 1 — FlexModels:** Pydantic OpenAPI models (usually automatic).
4. **Layer 0 — Transport:** `API`, `endpoints.*`, `SaxoAuthClient`.

Rule: start at Layer 3; drop to Layer 2/0 only for uncovered edge cases.

---

## SaxoClient — minimal patterns

```python
from saxo_api_client.contrib.client import SaxoClient

client = SaxoClient(access_token="...")  # or auth_client=SaxoAuthClient(...)

# amount > 0 Buy, amount < 0 Sell
client.market_order(asset_type="FxSpot", uic=21, amount=10000)
client.limit_order(asset_type="FxSpot", uic=21, amount=10000, order_price=1.10)
client.stop_order(asset_type="FxSpot", uic=21, amount=-10000, order_price=1.09)
client.stop_limit_order(
    asset_type="CfdOnStock", uic=211, amount=-1,
    order_price=150.0, stop_limit_price=149.5,
)
client.validate_order(order_builder_instance)  # PrecheckOrder, no fill
client.cancel_order(order_id)
```

Keyword style: `asset_type` first; resolve with `symbol=` and/or `uic=`.

`IsForceOpen`: stripped automatically for Stock; allowed for FX/CFD (hedging).

---

## Pitfalls (read before placing orders)

- Prefer **simulation** tokens and `validate_order` before live placement.
- Rate limits: SessionOrders is strict; space order calls (~1s).
- Do not invent undocumented fields; prefer Layer 3 methods.
- Streaming helpers are incomplete — do not rely on them for production market data.
- Wheel does **not** ship full `docs/` or `.ai/`; this GUIDE + README are the installed agent sources. Clone the repo for full docs.

---

## How to deepen (if repo or docs available)

1. **MCP (preferred for agents):** PyPI `mcp-server-saxo-openapi` — endpoint search, nested specs, `saxo://docs/pitfalls.md`. Not a trading client.
2. README 3-tier section and this GUIDE  
3. `docs/contrib/client.md` / `option_trader.md` (clone)  
4. Human browsing: [SaxoBank OpenAPI Docs Markdown](https://github.com/nohikomiso/SaxoBank-OpenAPI-Docs) or [official reference](https://www.developer.saxo/openapi/referencedocs)

Do **not** treat removed `SaxoTrader` docs/samples as current API.
