"""Tests for optional API exchange tracing."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest
from saxo_openapi.exceptions import OpenAPIError
from saxo_openapi.saxo_openapi import API
from saxo_openapi.trace import (
    ApiTraceWriter,
    endpoint_label,
    mask_secrets,
    resolve_trace_writer,
)


class _FakeEndpoint:
    method = "GET"
    _endpoint = "/port/v1/accounts/me"

    def __init__(self) -> None:
        self.params = {"AccountKey": "ACC-1"}
        self.data = None
        self.response = None
        self.status_code = None


def test_mask_secrets_nested() -> None:
    data = {"AccountKey": "k", "nested": {"access_token": "t", "ok": 1}}
    masked = mask_secrets(data)
    assert masked["AccountKey"] == "***MASKED***"
    assert masked["nested"]["access_token"] == "***MASKED***"
    assert masked["nested"]["ok"] == 1


def test_resolve_trace_writer_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv("SAXO_OPENAPI_TRACE", raising=False)
    assert resolve_trace_writer(None, None) is None

    monkeypatch.setenv("SAXO_OPENAPI_TRACE", "1")
    monkeypatch.setenv("SAXO_OPENAPI_TRACE_DIR", str(tmp_path))
    writer = resolve_trace_writer(None, None)
    assert writer is not None
    assert writer._root_dir == tmp_path


def test_resolve_trace_dir_arg_overrides_env_off(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SAXO_OPENAPI_TRACE", "0")
    writer = resolve_trace_writer(tmp_path, None)
    assert writer is not None


def test_api_trace_writes_roundtrip(tmp_path: Path) -> None:
    writer = ApiTraceWriter(tmp_path)
    endpoint = _FakeEndpoint()
    pending = writer.begin(endpoint, method="get", url="https://example/port/v1/accounts/me", request_args={"params": endpoint.params})
    writer.write_success(
        pending,
        status_code=200,
        response_headers={"X-Correlation": "corr-1"},
        body={"Data": []},
        duration_ms=12.5,
    )

    day_dirs = list(tmp_path.iterdir())
    assert len(day_dirs) == 1
    files = list(day_dirs[0].glob("saxo_*.json"))
    assert len(files) == 1
    payload = json.loads(files[0].read_text(encoding="utf-8"))
    assert payload["broker"] == "saxo"
    assert payload["request"]["params"]["AccountKey"] == "***MASKED***"
    assert payload["response"]["headers"]["X-Correlation"] == "corr-1"
    assert payload["meta"]["duration_ms"] == 12.5


def test_api_trace_openapi_error(tmp_path: Path) -> None:
    writer = ApiTraceWriter(tmp_path)
    endpoint = _FakeEndpoint()
    pending = writer.begin(endpoint, method="post", url="https://example/port/v1/orders", request_args={"json": {"AccountKey": "ACC"}})
    writer.write_openapi_error(
        pending,
        exc=OpenAPIError(400, "Bad Request", '{"ErrorCode":"X"}'),
        duration_ms=3.0,
    )
    files = list((tmp_path / list(tmp_path.iterdir())[0].name).glob("*.json"))
    payload = json.loads(files[0].read_text(encoding="utf-8"))
    assert payload["response"]["status_code"] == 400
    assert payload["meta"]["error"]["type"] == "OpenAPIError"


def test_api_request_records_on_openapi_error(tmp_path: Path) -> None:
    api = API(access_token="secret-token", trace_dir=str(tmp_path), trace_enabled=True)
    endpoint = _FakeEndpoint()

    with patch.object(API, "_API__request", side_effect=OpenAPIError(400, "Bad Request", '{"Message":"fail"}')), pytest.raises(OpenAPIError):
        api.request(endpoint)

    day_dir = next(tmp_path.iterdir())
    files = list(day_dir.glob("*.json"))
    assert len(files) == 1
    payload = json.loads(files[0].read_text(encoding="utf-8"))
    assert payload["response"]["status_code"] == 400


def test_api_no_trace_files_when_disabled(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SAXO_OPENAPI_TRACE", raising=False)
    api = API(access_token="t", trace_enabled=False)
    assert api._trace_writer is None


def test_endpoint_label() -> None:
    assert endpoint_label(_FakeEndpoint()) == "port_v1_accounts_me"
