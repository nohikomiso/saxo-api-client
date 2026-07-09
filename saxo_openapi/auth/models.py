"""Data Models for Saxo OpenAPI Authentication.

Migrated from saxo-apy (https://github.com/nohikomiso/saxo-apy).
Original copyright (c) 2022 Gid van der Ven, MIT License.
Modifications (c) 2025 nohikomiso, MIT License.
"""

import json
from base64 import urlsafe_b64decode
from datetime import datetime
from enum import Enum
from time import time
from typing import Any

from pydantic import (
    AnyHttpUrl,
    AnyUrl,
    BaseModel,
    ConfigDict,
    Field,
    GetCoreSchemaHandler,
    field_validator,
    model_validator,
)
from pydantic_core import core_schema

SIM_STREAMING_URL = "wss://streaming.saxobank.com/sim/oapi/streaming/ws"
LIVE_STREAMING_URL = "wss://streaming.saxobank.com/oapi/streaming/ws"


class ClientId(str):
    """ClientId. 32 char string."""

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler: GetCoreSchemaHandler):
        def validate(v):
            import re

            if not re.match(r"^[a-f0-9]{32}$", v):
                raise ValueError("Invalid ClientId format")
            return v

        return core_schema.no_info_plain_validator_function(validate)


class ClientSecret(ClientId):
    """CLientSecret. Same as ClientId."""

    pass


class HttpsUrl(AnyUrl):
    """HTTPS URL. Override AnyUrl to only allow for secure protocol."""

    allowed_schemes = {"https"}


class GrantType(Enum):
    """OAuth grant type. Only supported version is Code."""

    CODE = "Code"


class APIEnvironment(Enum):
    """OpenAPI Environment. SIM and LIVE are currently supported."""

    SIM = "SIM"
    LIVE = "LIVE"


class AuthorizationCode(str):
    """Auth code. GUID."""

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler: GetCoreSchemaHandler):
        def validate(v):
            import re

            if not re.match(r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$", v):
                raise ValueError("Invalid AuthorizationCode format")
            return v

        return core_schema.no_info_plain_validator_function(validate)


class RefreshToken(AuthorizationCode):
    """Refresh token. Same as Auth code (GUID)."""

    pass


class AuthorizationType(Enum):
    """Supported auth types. Either a auth code or refresh token can be exercised."""

    CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"


class OpenAPIAppConfig(BaseModel):
    """Dataclass for parsing and validating app config objects."""

    model_config = ConfigDict(extra="forbid")
    app_name: str = Field(..., alias="AppName")
    grant_type: GrantType = Field(..., alias="GrantType")
    client_id: ClientId = Field(..., alias="AppKey")
    client_secret: ClientSecret = Field(..., alias="AppSecret")
    auth_endpoint: HttpsUrl = Field(..., alias="AuthorizationEndpoint")
    token_endpoint: HttpsUrl = Field(..., alias="TokenEndpoint")
    api_base_url: HttpsUrl = Field(..., alias="OpenApiBaseUrl")
    streaming_url: HttpsUrl | None = None
    redirect_urls: list[AnyHttpUrl] = Field(..., alias="RedirectUrls")
    env: APIEnvironment | None = None

    @model_validator(mode="after")
    def validate_redirect_urls_contains_localhost(self):
        """Redirect URLs must at least have 1 localhost available."""
        available_hosts = [url.host for url in self.redirect_urls]
        assert "localhost" in available_hosts, f"at least 1 'localhost' redirect URL required in app config - hosts: {available_hosts}"
        return self

    @model_validator(mode="after")
    def validate_port_configuration_redirect_urls(self):
        """Port configuration validation - only warn for HTTP URLs without explicit ports."""
        for url in self.redirect_urls:
            url_str = str(url)
            if url.scheme == "https":
                continue
            if url.scheme == "http" and ":" + str(url.port) not in url_str:
                pass
        return self

    @model_validator(mode="after")
    def strip_base_url_suffix(self) -> "OpenAPIAppConfig":
        """Strip forward slash form base URL."""
        if self.api_base_url:
            self.api_base_url = HttpsUrl(str(self.api_base_url).rstrip("/"))
        return self

    @model_validator(mode="after")
    def derive_env_fields(self) -> "OpenAPIAppConfig":
        """Set environment and streaming URL based on environment."""
        if "sim.logonvalidation" in str(self.auth_endpoint):
            self.env = APIEnvironment.SIM
            self.streaming_url = HttpsUrl(SIM_STREAMING_URL)
        if "live.logonvalidation" in str(self.auth_endpoint):
            self.env = APIEnvironment.LIVE
            self.streaming_url = HttpsUrl(LIVE_STREAMING_URL)
        return self

    @classmethod
    def parse_obj(cls, obj: Any) -> "OpenAPIAppConfig":
        """Pydantic v1 compatibility shim."""
        try:
            return cls.model_validate(obj)
        except Exception as e:
            from loguru import logger
            logger.error(f"OpenAPIAppConfig.parse_obj互換レイヤーでのエラー: {e}")
            raise


class TokenData(BaseModel):
    """Dataclass for parsing token data."""

    access_token: str
    token_type: str
    expires_in: int
    refresh_token: RefreshToken
    refresh_token_expires_in: int
    base_uri: HttpsUrl | None
    access_token_expiry: int
    refresh_token_expiry: int
    client_key: str
    user_key: str
    session_id: str
    write_permission: bool

    @model_validator(mode="before")
    def set_fields_from_token_payload(cls, values: dict) -> dict:
        """Set fields from token claims."""
        token_bytes = values["access_token"].encode("utf-8")
        payload = token_bytes.split(b".")[1]
        padded = payload + b"=" * divmod(len(payload), 4)[1]
        decoded = urlsafe_b64decode(padded)
        claims = json.loads(decoded.decode("utf-8"))

        values["access_token_expiry"] = claims["exp"]
        values["refresh_token_expiry"] = int(time()) + values["refresh_token_expires_in"]
        values["client_key"] = claims["cid"]
        values["user_key"] = claims["uid"]
        values["session_id"] = claims["sid"]
        values["write_permission"] = claims.get("oaa") == "77770"

        return values

    @classmethod
    def parse_obj(cls, obj: Any) -> "TokenData":
        """Pydantic v1 compatibility shim."""
        try:
            return cls.model_validate(obj)
        except Exception as e:
            from loguru import logger
            logger.error(f"TokenData.parse_obj互換レイヤーでのエラー: {e}")
            raise


class NotLoggedInError(Exception):
    """Client is not logged in."""
    pass


class TokenExpiredError(Exception):
    """Token has expired and can no longer be used."""
    pass


class APIRequestError(Exception):
    """An error occurred while creating the OpenAPI request."""
    pass


class APIResponseError(Exception):
    """An error occurred while executing the OpenAPI request."""
    pass
