#!/usr/bin/env python3
"""Offline demo: API trace files are written without network calls.

Usage:
    uv run python libs/saxo_openapi/samples/verify_trace_offline.py

Writes one sample trace under ./api_traces/ (or SAXO_OPENAPI_TRACE_DIR).
"""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from saxo_openapi.trace import ApiTraceWriter, endpoint_label


class _DemoEndpoint:
    method = "GET"
    _endpoint = "/root/v1/diagnostics"

    params: dict[str, str] | None = None
    data = None


def main() -> int:
    out_root = Path(tempfile.mkdtemp(prefix="saxo_trace_demo_"))
    writer = ApiTraceWriter(out_root)
    ep = _DemoEndpoint()
    pending = writer.begin(
        ep,
        method="get",
        url="https://gateway.saxobank.com/sim/openapi/root/v1/diagnostics",
        request_args={"params": None},
    )
    writer.write_success(
        pending,
        status_code=200,
        response_headers={"X-Correlation": "demo-correlation"},
        body={"State": "Ok"},
        duration_ms=1.0,
    )

    day_dir = next(out_root.iterdir())
    trace_file = next(day_dir.glob("saxo_*.json"))
    payload = json.loads(trace_file.read_text(encoding="utf-8"))
    print(json.dumps({"trace_dir": str(out_root), "api": endpoint_label(ep), "file": str(trace_file), "payload": payload}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
