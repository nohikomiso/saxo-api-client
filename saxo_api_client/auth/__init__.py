"""saxo_api_client.auth — Saxo OpenAPI 認証サブモジュール。

使用例::

    from saxo_api_client.auth import SaxoAuthClient
    from saxo_api_client.auth.models import TokenData, TokenExpiredError
    from saxo_api_client.auth.utils import construct_auth_url, validate_redirect_url
"""

from .client import SaxoAuthClient, SaxoOpenAPIClient
from .models import (
    APIEnvironment,
    AuthorizationCode,
    NotLoggedInError,
    OpenAPIAppConfig,
    TokenData,
    TokenExpiredError,
)
from .utils import construct_auth_url, validate_redirect_url

__all__ = [
    # クライアント
    "SaxoAuthClient",
    "SaxoOpenAPIClient",  # 後方互換エイリアス
    # モデル
    "APIEnvironment",
    "AuthorizationCode",
    "NotLoggedInError",
    "OpenAPIAppConfig",
    "TokenData",
    "TokenExpiredError",
    # ユーティリティ
    "construct_auth_url",
    "validate_redirect_url",
]
