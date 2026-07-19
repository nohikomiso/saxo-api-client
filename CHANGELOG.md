# Changelog

## Unreleased

### Changed

- **Breaking:** `SaxoTrader` (`contrib.trader`) remains removed. Use `SaxoClient` (`contrib.client`). No compatibility shim.
- Docs (EN/JA): Layer 3 documented as `SaxoClient` + `OptionTrader`.
- Samples `verify_orders_live.py` / `verify_orders_precheck.py` migrated to `SaxoClient`.
- `SaxoClient.place_order` deduplicated and routed through `_execute_order` (AccountKey binding).

### Added

- `SaxoClient.validate_order`, `stop_limit_order`, `stop_if_traded_order`.
- `docs/contrib/client.md` as the Layer 3 FX/Stock/CFD reference.

## 1.0.0 — 2026-07-10

### Changed

- **Package rename:** PyPI `saxo-api-client`, import `saxo_api_client` (formerly `saxo-openapi` / `saxo_openapi` fork).
- **Breaking:** Not compatible with hootnot `saxo-api-client` 0.6.0 on PyPI. See README migration notes.
- `saxo_api_client.py` core module renamed to `client.py` (`from saxo_api_client import API` unchanged).

### Added

- `pyproject.toml` (hatchling) packaging for PyPI distribution.
