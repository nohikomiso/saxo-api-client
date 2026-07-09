"""Saxo Bank OpenAPI Authentication Client.

Migrated from saxo-apy (https://github.com/nohikomiso/saxo-apy).
Original copyright (c) 2022 Gid van der Ven, MIT License.
Modifications (c) 2025 nohikomiso, MIT License.

このモジュールは認証（OAuth2 ログイン・トークン取得・リフレッシュ）機能のみを提供します。
API リクエスト（GET/POST 等）は saxo_openapi 本体の機能を使用してください。
"""

import asyncio
import json
import threading
import webbrowser
from collections.abc import Callable
from datetime import datetime
from secrets import token_urlsafe
from time import sleep, time
from urllib.parse import parse_qs

from httpx import post
from loguru import logger
from pydantic import AnyHttpUrl, ValidationError

from .models import (
    APIEnvironment,
    AuthorizationCode,
    NotLoggedInError,
    OpenAPIAppConfig,
    TokenData,
    TokenExpiredError,
)
from .redirect_server import RedirectServer
from .utils import (
    configure_logger,
    construct_auth_url,
    parse_obj_as,
    unix_seconds_to_datetime,
    validate_redirect_url,
)

logger.remove()  # デフォルトのコンソールロガーを削除


class SaxoAuthClient:
    """Saxo OpenAPI 認証クライアント。

    OAuth2 によるログイン・トークン取得・リフレッシュを担当します。
    API リクエストは saxo_openapi 本体の機能（API）を使用してください。

    Parameters
    ----------
    app_config:
        Developer Portal から取得したアプリ設定。辞書またはJSONファイルパス。
        デフォルトは "app_config.json"。
    log_sink:
        ログ出力先（ファイルパス等）。省略時はログ出力なし。
    log_level:
        ログレベル（DEBUG / INFO / WARNING / ERROR）。デフォルト "DEBUG"。
    """

    def __init__(
        self,
        app_config: dict | str | None = "app_config.json",
        log_sink: str | None = None,
        log_level: str = "DEBUG",
        on_token_refresh: Callable[[TokenData], None] | None = None,
    ) -> None:
        if log_sink:
            configure_logger(log_sink, log_level)
            
        self.on_token_refresh = on_token_refresh

        self.client_session_id: str = token_urlsafe(10)
        logger.debug(f"initializing Auth Client with session id: {self.client_session_id}")

        self._app_config: OpenAPIAppConfig

        try:
            if isinstance(app_config, dict):
                logger.debug("辞書からアプリ設定を初期化")
                self._app_config = parse_obj_as(OpenAPIAppConfig, app_config)
            elif isinstance(app_config, str):
                logger.debug(f"ファイルからアプリ設定を初期化: {app_config}")
                with open(app_config) as f:
                    config = json.load(f)
                self._app_config = parse_obj_as(OpenAPIAppConfig, config)
            else:
                raise RuntimeError(f"invalid type provided for 'app_config': {type(app_config)}")
        except Exception as e:
            logger.error(f"アプリ設定の初期化に失敗: {e}")
            raise

        self._token_data: TokenData | None = None
        logger.success("successfully parsed app config and initialized Auth Client")

    # ------------------------------------------------------------------ #
    # ログイン・ログアウト                                                  #
    # ------------------------------------------------------------------ #

    def login(
        self,
        redirect_url: AnyHttpUrl | None = None,
        launch_browser: bool = True,
        catch_redirect: bool = True,
        start_async_refresh: bool = False,
    ) -> None:
        """Saxo OpenAPI へ OAuth2 ログインします。

        Parameters
        ----------
        redirect_url:
            ログイン後のリダイレクト先。省略時は設定の最初の localhost URL。
        launch_browser:
            True でブラウザを自動で開きます。
        catch_redirect:
            True でリダイレクトを受け取るローカルサーバーを起動します。
        start_async_refresh:
            True でアクセストークンの自動リフレッシュを開始します（Jupyter 向け）。
        """
        logger.debug(f"initializing login sequence with {redirect_url=}, {launch_browser=} {catch_redirect=} {start_async_refresh=}")
        _redirect_url = validate_redirect_url(self._app_config, redirect_url)
        state = token_urlsafe(20)
        auth_url = construct_auth_url(self._app_config, _redirect_url, state)
        logger.debug(f"logging in with {str(_redirect_url)=} and {str(auth_url)=}")

        if catch_redirect:
            redirect_server = RedirectServer(_redirect_url, state=state)
            redirect_server.start()

        if launch_browser:
            logger.debug("launching browser with login page")
            print("🌐 opening login page in browser - waiting for user to authenticate... 🔑")
            webbrowser.open_new(str(auth_url))
        else:
            print(f"🌐 navigate to the following web page to log in: {auth_url}")

        if catch_redirect:
            try:
                while not redirect_server.auth_code:
                    sleep(0.1)
                print("📞 received callback from Saxo SSO")
                _auth_code = parse_obj_as(AuthorizationCode, redirect_server.auth_code)
            except KeyboardInterrupt:
                print("🛑 operation interrupted by user - shutting down")
                return
            finally:
                redirect_server.shutdown()
        else:
            auth_code_obtained = False
            while not auth_code_obtained:
                try:
                    user_input = input("📋 認証コードまたはリダイレクトURLを貼り付けてください: ").strip()

                    if user_input.startswith(("http://", "https://")):
                        redirect_location = parse_obj_as(AnyHttpUrl, user_input)
                        parsed_qs = parse_qs(redirect_location.query)
                        _auth_code = parse_obj_as(AuthorizationCode, parsed_qs["code"][0])
                    else:
                        _auth_code = parse_obj_as(AuthorizationCode, user_input)

                    auth_code_obtained = True

                except ValidationError as e:
                    print(f"❌ 入力形式が正しくありません。認証コード（GUID形式）またはリダイレクトURLを入力してください: {e}")
                except (KeyError, IndexError):
                    print("❌ URLにcodeパラメータが見つかりません。正しいリダイレクトURLを入力してください。")
                except KeyboardInterrupt:
                    print("🛑 operation interrupted by user - shutting down")
                    return

        self.get_tokens(auth_code=_auth_code)

        assert self._token_data

        env = self._app_config.env.value  # type: ignore[union-attr]
        perm = "WRITE / TRADE" if self._token_data.write_permission else "READ"

        print(f"✅ authorization succeeded - connected to {env} environment with {perm} permissions (session ID {self._token_data.session_id})")

        if self._app_config.env is APIEnvironment.LIVE and self._token_data.write_permission:
            print("❗ NOTE: you are now connected to a real-money client in the LIVE environment with WRITE & TRADE permissions")

        if start_async_refresh:
            asyncio.create_task(self.async_refresh(), name="async_refresh")

        logger.success("login completed successfully")

    def logout(self) -> None:
        """セッションをリセットしてトークンを削除します。"""
        assert self.logged_in
        logger.debug("disconnecting from OpenAPI")
        self._token_data = None
        refresh_thread = [thread for thread in threading.enumerate() if thread.name == "RefreshThread"]
        if len(refresh_thread) > 0 and refresh_thread[0].is_alive():
            refresh_thread[0].cancel()  # type: ignore[attr-defined]
        logger.success("logout completed")

    # ------------------------------------------------------------------ #
    # トークン取得・リフレッシュ                                            #
    # ------------------------------------------------------------------ #

    def refresh(self) -> None:
        """リフレッシュトークンを使ってアクセストークンを更新します。"""
        logger.debug("refreshing API session")

        if not self._token_data:
            raise NotLoggedInError("no active session found - connect the client with '.login()'")

        if time() > self._token_data.refresh_token_expiry:
            raise TokenExpiredError("refresh token has expired - reconnect the client with '.login()'")

        self.get_tokens()
        logger.debug("successfully refreshed API session")

    async def async_refresh(self) -> None:
        """アクセストークンを非同期で自動リフレッシュします（Jupyter 向け）。"""
        while self._token_data and self.refresh_token_valid:
            current_time = int(time())
            time_to_expiry = self._token_data.access_token_expiry - current_time
            delay = max(time_to_expiry - 30, 1)
            logger.debug(f"async refresh will kick off refresh flow in {delay} seconds at: {unix_seconds_to_datetime(current_time + delay)}")
            await asyncio.sleep(delay)

            if not self.refresh_token_valid:
                logger.warning("refresh token expired - stopping async refresh")
                break

            logger.debug("async refresh delay has passed - kicking off refresh")
            try:
                self.refresh()
            except TokenExpiredError:
                logger.error("refresh token expired during async refresh - stopping")
                break
        logger.debug("async refresh stopped")

    def get_tokens(self, auth_code: AuthorizationCode | None = None) -> None:
        """認証コードまたはリフレッシュトークンを使ってトークンペアを取得します。"""
        authorization_param = "code" if auth_code else "refresh_token"
        grant_type = "authorization_code" if auth_code else "refresh_token"
        logger.debug(f"exercising authorization with grant type: {grant_type}")

        token_request_params = {
            "grant_type": grant_type,
            authorization_param: auth_code or self._token_data.refresh_token,  # type: ignore[union-attr]
            "client_id": self._app_config.client_id,
            "client_secret": self._app_config.client_secret,
        }
        response = post(
            str(self._app_config.token_endpoint),
            params=token_request_params,
            headers={
                "user-agent": "saxo-openapi-auth/1.0",
            },
        )

        if response.status_code == 401:
            raise TokenExpiredError("refresh token has expired or is invalid - reconnect the client with '.login()'")
        elif response.status_code != 201:
            try:
                error_detail = response.json()
                error_message = error_detail.get("error_description", "unknown error")
            except Exception:
                error_message = f"HTTP {response.status_code}"

            raise RuntimeError(f"unexpected error occurred while retrieving token - response status: {response.status_code}, detail: {error_message}")
        logger.success("successfully exercised authorization - new token data retrieved")

        received_token_data = response.json()
        try:
            self._token_data = TokenData.model_validate(received_token_data)
            logger.debug("Token data validated successfully with model_validate")
            if self.on_token_refresh:
                try:
                    self.on_token_refresh(self._token_data)
                except Exception as e:
                    logger.error(f"Error in on_token_refresh callback: {e}")
        except Exception as e:
            logger.error(f"Failed to validate token data: {e}")
            raise RuntimeError(f"トークンデータの検証に失敗しました: {e}") from e

    # ------------------------------------------------------------------ #
    # プロパティ                                                            #
    # ------------------------------------------------------------------ #

    @property
    def available_redirect_urls(self) -> list[AnyHttpUrl]:
        """設定から利用可能なリダイレクトURLを返します。"""
        return self._app_config.redirect_urls

    @property
    def logged_in(self) -> bool:
        """有効なセッションがあるか確認します。"""
        if not self._token_data:
            raise NotLoggedInError("no active session found - connect the client with '.login()'")
        if time() > self._token_data.access_token_expiry:
            raise TokenExpiredError("access token has expired - reconnect the client with '.login()'")
        return True

    @property
    def access_token(self) -> str:
        """現在有効なアクセストークンを返します。"""
        assert self.logged_in
        assert self._token_data
        return self._token_data.access_token

    @property
    def token_data(self) -> TokenData:
        """トークンデータ全体を返します。"""
        assert self.logged_in
        assert self._token_data
        return self._token_data

    @property
    def access_token_expiry(self) -> datetime:
        """アクセストークンの有効期限（datetime）を返します。"""
        assert self.logged_in
        return unix_seconds_to_datetime(
            self._token_data.access_token_expiry  # type: ignore[union-attr]
        )

    @property
    def time_to_expiry(self) -> int:
        """アクセストークンの残り有効秒数を返します。"""
        assert self.logged_in
        token_expiry = self._token_data.access_token_expiry  # type: ignore[union-attr]
        return token_expiry - int(time())

    @property
    def refresh_token_valid(self) -> bool:
        """リフレッシュトークンがまだ有効かどうかを返します。"""
        if not self._token_data:
            return False
        return time() <= self._token_data.refresh_token_expiry


# 後方互換性のためのエイリアス
# 旧コードが `SaxoOpenAPIClient` でインポートしていた箇所に対応
SaxoOpenAPIClient = SaxoAuthClient
