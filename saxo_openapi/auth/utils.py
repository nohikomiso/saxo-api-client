"""Utils for Saxo OpenAPI Authentication.

Migrated from saxo-apy (https://github.com/nohikomiso/saxo-apy).
Original copyright (c) 2022 Gid van der Ven, MIT License.
Modifications (c) 2025 nohikomiso, MIT License.
"""

from datetime import UTC, datetime
from typing import Any, TypeVar
from urllib.parse import urlencode

from loguru import logger
from pydantic import AnyHttpUrl, TypeAdapter

from .models import HttpsUrl, OpenAPIAppConfig

T = TypeVar("T")


def parse_obj_as(type_: type, obj: Any) -> Any:
    """Pydantic v1 compatibility shim using TypeAdapter.validate_python."""
    try:
        adapter = TypeAdapter(type_)
        return adapter.validate_python(obj)
    except Exception as e:
        logger.error(f"parse_obj_as互換関数でのエラー: {e}")
        raise


def configure_logger(log_sink: str, log_level: str) -> None:
    """Set defaults for log config."""
    logger.add(
        log_sink,
        format=("{time:YYYY-MM-DD HH:mm:ss.SSS!UTC}Z {thread:12} {level:8} {module:15} {line:3} {function:25} {message}"),
        level=log_level,
        enqueue=True,
    )


def unix_seconds_to_datetime(timestamp: int) -> datetime:
    """Convert unix seconds to human-readable timestamp."""
    return datetime.fromtimestamp(timestamp, tz=UTC)


def validate_redirect_url(app_config: OpenAPIAppConfig, redirect_url: AnyHttpUrl | None) -> AnyHttpUrl:
    """Check if provided redirect URL for login is valid - or default to config."""
    if not redirect_url:
        logger.debug("no redirect URL provided - defaulting to first localhost in config")
        _redirect_url: AnyHttpUrl = [url for url in app_config.redirect_urls if url.host == "localhost"][0]
    else:
        assert redirect_url in app_config.redirect_urls, f"redirect url {redirect_url} not available in app config - see client.available_redirect_urls"
        _redirect_url = redirect_url
    return _redirect_url


def construct_auth_url(app_config: OpenAPIAppConfig, redirect_url: AnyHttpUrl, state: str) -> HttpsUrl:
    """Parse app_config to generate auth URL."""
    auth_request_query_params = {
        "response_type": "code",
        "client_id": app_config.client_id,
        "state": state,
        "redirect_uri": str(redirect_url),
    }

    return parse_obj_as(
        HttpsUrl,
        str(app_config.auth_endpoint) + "?" + urlencode(auth_request_query_params),
    )
