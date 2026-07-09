"""Optional REST exchange tracing for Saxo OpenAPI client (research / debugging)."""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from secrets import token_hex
from typing import Any

MASK_VALUE = "***MASKED***"

SENSITIVE_FIELDS = frozenset(
    {
        "access_token",
        "AccessToken",
        "refresh_token",
        "RefreshToken",
        "AccountKey",
        "ClientKey",
        "Token",
        "authorization",
        "Authorization",
        "password",
        "Password",
    }
)

_RESPONSE_HEADER_KEYS = frozenset(
    {
        "x-correlation",
        "x-request-id",
    }
)

_ENV_TRACE = "SAXO_OPENAPI_TRACE"
_ENV_TRACE_DIR = "SAXO_OPENAPI_TRACE_DIR"
_DEFAULT_TRACE_DIR = "api_traces"


def _truthy_env(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def resolve_trace_writer(
    trace_dir: str | Path | None,
    trace_enabled: bool | None,
) -> ApiTraceWriter | None:
    """Return a trace writer when tracing is enabled, else None."""
    if trace_enabled is False:
        return None
    if trace_enabled is True or (trace_enabled is None and _truthy_env(_ENV_TRACE)):
        root = trace_dir if trace_dir is not None else os.getenv(_ENV_TRACE_DIR, _DEFAULT_TRACE_DIR)
        return ApiTraceWriter(Path(root))
    if trace_dir is not None:
        return ApiTraceWriter(Path(trace_dir))
    return None


def mask_secrets(data: Any) -> Any:
    """Recursively mask sensitive fields in dict/list structures."""
    if isinstance(data, dict):
        masked: dict[str, Any] = {}
        for key, value in data.items():
            if key in SENSITIVE_FIELDS:
                masked[key] = MASK_VALUE
            else:
                masked[key] = mask_secrets(value)
        return masked
    if isinstance(data, list):
        return [mask_secrets(item) for item in data]
    return data


def endpoint_label(endpoint: Any) -> str:
    """Stable label for trace files (path or class name)."""
    if hasattr(endpoint, "_endpoint"):
        path = str(endpoint._endpoint)
        slug = path.strip("/").replace("/", "_")
        if slug:
            return slug
    return type(endpoint).__name__


def _slugify(value: str, max_len: int = 80) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")
    return slug[:max_len] if slug else "api"


def _new_trace_id() -> str:
    ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return f"{ts}-{token_hex(4)}"


def _pick_response_headers(headers: Any) -> dict[str, str]:
    picked: dict[str, str] = {}
    if not headers:
        return picked
    try:
        items = headers.items()
    except AttributeError:
        return picked
    for key, value in items:
        if str(key).lower() in _RESPONSE_HEADER_KEYS:
            picked[str(key)] = str(value)
    return picked


def _parse_error_body(content: str | None) -> Any:
    if not content:
        return None
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return content[:8000] if len(content) > 8000 else content


@dataclass(frozen=True)
class _PendingTrace:
    trace_id: str
    api: str
    method: str
    url: str
    params: Any
    body: Any


class ApiTraceWriter:
    """Writes one JSON file per REST round-trip under {root}/{YYYYMMDD}/."""

    def __init__(self, root_dir: Path) -> None:
        self._root_dir = Path(root_dir)

    @property
    def enabled(self) -> bool:
        return True

    def begin(
        self,
        endpoint: Any,
        *,
        method: str,
        url: str,
        request_args: dict[str, Any],
    ) -> _PendingTrace:
        params = request_args.get("params")
        body = request_args.get("json")
        return _PendingTrace(
            trace_id=_new_trace_id(),
            api=endpoint_label(endpoint),
            method=method.upper(),
            url=url,
            params=mask_secrets(params),
            body=mask_secrets(body),
        )

    def write_success(
        self,
        pending: _PendingTrace,
        *,
        status_code: int,
        response_headers: Any,
        body: Any,
        duration_ms: float,
    ) -> None:
        payload = self._build_payload(
            pending,
            duration_ms=duration_ms,
            response={
                "status_code": status_code,
                "headers": _pick_response_headers(response_headers),
                "body": mask_secrets(body),
            },
            error=None,
        )
        self._write_file(pending, payload)

    def write_openapi_error(
        self,
        pending: _PendingTrace,
        *,
        exc: Any,
        duration_ms: float,
    ) -> None:
        code = getattr(exc, "code", None)
        reason = getattr(exc, "reason", None)
        content = getattr(exc, "content", None)
        payload = self._build_payload(
            pending,
            duration_ms=duration_ms,
            response={
                "status_code": code,
                "headers": {},
                "body": mask_secrets(_parse_error_body(content)),
            },
            error={"type": type(exc).__name__, "reason": reason, "code": code},
        )
        self._write_file(pending, payload)

    def write_request_exception(
        self,
        pending: _PendingTrace,
        *,
        exc: BaseException,
        duration_ms: float,
    ) -> None:
        payload = self._build_payload(
            pending,
            duration_ms=duration_ms,
            response={"status_code": None, "headers": {}, "body": None},
            error={"type": type(exc).__name__, "message": str(exc)},
        )
        self._write_file(pending, payload)

    def write_stream_skipped(self, endpoint: Any, *, url: str, method: str) -> None:
        """Record a one-line note that streaming was not fully captured (phase 1)."""
        pending = _PendingTrace(
            trace_id=_new_trace_id(),
            api=endpoint_label(endpoint),
            method=method.upper(),
            url=url,
            params=None,
            body=None,
        )
        payload = self._build_payload(
            pending,
            duration_ms=0.0,
            response={
                "status_code": None,
                "headers": {},
                "body": {"note": "streaming endpoint; full body not recorded in phase 1"},
            },
            error=None,
        )
        self._write_file(pending, payload)

    def _build_payload(
        self,
        pending: _PendingTrace,
        *,
        duration_ms: float,
        response: dict[str, Any],
        error: dict[str, Any] | None,
    ) -> dict[str, Any]:
        return {
            "trace_id": pending.trace_id,
            "broker": "saxo",
            "api": pending.api,
            "request": {
                "method": pending.method,
                "url": pending.url,
                "params": pending.params,
                "body": pending.body,
            },
            "response": response,
            "meta": {
                "duration_ms": round(duration_ms, 2),
                "error": error,
            },
        }

    def _write_file(self, pending: _PendingTrace, payload: dict[str, Any]) -> None:
        day = datetime.now(UTC).strftime("%Y%m%d")
        out_dir = self._root_dir / day
        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            slug = _slugify(pending.api)
            filename = f"saxo_{slug}_{pending.trace_id}.json"
            path = out_dir / filename
            with path.open("w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
        except OSError:
            # Tracing must not break API calls.
            return
