# Changelog

## 1.0.0 — 2026-07-10

### Changed

- **Package rename:** PyPI `saxo-api-client`, import `saxo_api_client` (formerly `saxo-openapi` / `saxo_openapi` fork).
- **Breaking:** Not compatible with hootnot `saxo-api-client` 0.6.0 on PyPI. See README migration notes.
- `saxo_api_client.py` core module renamed to `client.py` (`from saxo_api_client import API` unchanged).

### Added

- `pyproject.toml` (hatchling) packaging for PyPI distribution.
