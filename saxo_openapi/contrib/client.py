from typing import Any, Optional

import saxo_openapi.definitions.orders as OD
import saxo_openapi.endpoints.portfolio as pf
import saxo_openapi.endpoints.referencedata as rd
import saxo_openapi.endpoints.trading as tr
from saxo_openapi import API
from saxo_openapi.auth.client import SaxoAuthClient
from saxo_openapi.contrib.orders import (
    LimitOrder,
    MarketOrder,
    StopIfTradedOrder,
    StopLimitOrder,
    StopOrder,
)
from saxo_openapi.contrib.orders.helper import tie_account_to_order
from saxo_openapi.contrib.util.instrument_to_uic import InstrumentToUic
from saxo_openapi.contrib.session import account_info

# NOTE: For MarketScheduleCache we import dynamically to avoid circular dependencies
# if trading_core is loaded later or as a separate package.
try:
    from trading_core.market.market_schedule import MarketScheduleCache
except ImportError:
    MarketScheduleCache = None


class SaxoClient:
    """
    SaxoClient is the ultimate facade for interacting with SaxoBank API.
    It encapsulates the raw API client, provides intuitive one-liner methods
    for querying balances, positions, market schedules, and placing orders.
    It completely hides the underlying "Command pattern" (Endpoint classes).
    """

    def __init__(self, auth_client: Optional[SaxoAuthClient] = None, access_token: Optional[str] = None):
        """
        Initialize the unified client.
        Either auth_client or access_token must be provided.
        """
        self._api = API(access_token=access_token, auth_client=auth_client)
        self._account_key = None
        self._instrument_cache: dict[str, dict] = {}
        
        # Initialize market schedule cache if available
        if MarketScheduleCache:
            self._market_schedule = MarketScheduleCache(self._api)
        else:
            self._market_schedule = None

    @property
    def account_key(self) -> str:
        """Get the default AccountKey, fetching it if necessary."""
        if self._account_key is None:
            self._account_key = account_info(self._api).AccountKey
        return self._account_key

    # ---------------------------------------------------------
    # Internal Helpers
    # ---------------------------------------------------------
    def _resolve_uic(self, Uic: Optional[int], Symbol: Optional[str], AssetType: str) -> int:
        """Resolve Uic from either explicit Uic or by querying the Symbol."""
        if Uic is not None:
            return Uic
        if Symbol is not None:
            spec = {"Instrument": Symbol}
            spec = InstrumentToUic(self._api, self.account_key, spec, assettype=AssetType)
            return spec["Uic"]
        raise ValueError("Either Uic or Symbol must be provided")

    def _execute_order(self, order_spec: dict | Any, validate_only: bool = False) -> dict:
        """Bind account and execute or precheck order."""
        order_spec_with_account = tie_account_to_order(self.account_key, order_spec)
        asset_type = order_spec_with_account.get("AssetType")
        
        if asset_type in [OD.AssetType.Stock, OD.AssetType.StockOption]:
            order_spec_with_account.pop("IsForceOpen", None)

        if validate_only:
            r = tr.orders.PrecheckOrder(data=order_spec_with_account)
        else:
            r = tr.orders.Order(data=order_spec_with_account)

        return self._api.request(r)

    # ---------------------------------------------------------
    # Portfolio & Account (Read Operations)
    # ---------------------------------------------------------
    def get_accounts(self) -> dict:
        """Get a list of all accounts."""
        r = pf.accounts.AccountsMe()
        return self._api.request(r)

    def get_account_balance(self, client_key: Optional[str] = None) -> dict:
        """Get the current balance and margin details for the account."""
        kwargs = {"ClientKey": client_key} if client_key else {}
        r = pf.balances.AccountBalancesMe(**kwargs)
        return self._api.request(r)

    def get_positions(self, client_key: Optional[str] = None) -> dict:
        """Get all open net positions."""
        kwargs = {"ClientKey": client_key} if client_key else {}
        r = pf.netpositions.NetPositionsMe(**kwargs)
        return self._api.request(r)

    def get_active_orders(self, client_key: Optional[str] = None, status: str = "Working") -> dict:
        """Get a list of active (working) orders."""
        kwargs = {"ClientKey": client_key, "Status": status} if client_key else {"Status": status}
        r = pf.orders.OrdersMe(**kwargs)
        return self._api.request(r)

    # ---------------------------------------------------------
    # Market Data & Schedule
    # ---------------------------------------------------------
    def get_instrument_details(self, asset_type: str, symbol: Optional[str] = None, uic: Optional[int] = None) -> dict:
        """Fetch detailed specifications (lot size, tick size, etc) for an instrument."""
        uic_resolved = self._resolve_uic(uic, symbol, asset_type)
        
        cache_key = f"{uic_resolved}_{asset_type}"
        if cache_key in self._instrument_cache:
            return self._instrument_cache[cache_key]

        params = {"AccountKey": self.account_key}
        r = rd.instruments.InstrumentDetails(Uic=uic_resolved, AssetType=asset_type, params=params)
        rv = self._api.request(r)
        self._instrument_cache[cache_key] = rv
        return rv

    def get_market_schedule(self, asset_type: str, symbol: Optional[str] = None, uic: Optional[int] = None) -> dict:
        """Fetch trading sessions/schedule for the instrument."""
        uic_resolved = self._resolve_uic(uic, symbol, asset_type)
        r = rd.instruments.TradingSchedule(Uic=uic_resolved, AssetType=asset_type)
        return self._api.request(r)

    def get_current_session_state(self, asset_type: str, symbol: Optional[str] = None, uic: Optional[int] = None) -> Optional[str]:
        """
        Get the raw state of the current trading session (e.g. 'AutomatedTrading', 'Closed').
        Leverages MarketScheduleCache if available.
        """
        uic_resolved = self._resolve_uic(uic, symbol, asset_type)
        
        if self._market_schedule:
            self._market_schedule.fetch_and_cache(uic_resolved, asset_type)
            session = self._market_schedule.get_current_session(uic_resolved, asset_type)
            if session:
                return session.get("State")
            return "Closed"
            
        # Fallback to direct API call if cache component not found
        schedule = self.get_market_schedule(asset_type=asset_type, uic=uic_resolved)
        sessions = schedule.get("Sessions", [])
        # Simplified fallback logic (assuming caller uses MarketScheduleCache in production)
        if not sessions:
            return "Closed"
        return sessions[0].get("State", "Closed")

    def is_order_accepted(self, asset_type: str, order_type: str, symbol: Optional[str] = None, uic: Optional[int] = None) -> bool:
        """
        Check if the specified order_type (e.g., 'Market', 'Limit') is currently accepted
        by the exchange for this instrument.
        """
        uic_resolved = self._resolve_uic(uic, symbol, asset_type)
        if self._market_schedule:
            self._market_schedule.fetch_and_cache(uic_resolved, asset_type)
            return self._market_schedule.is_market_open(uic=uic_resolved, asset_type=asset_type, order_type=order_type)
        
        # Fallback: Just check if state is AutomatedTrading
        state = self.get_current_session_state(asset_type=asset_type, uic=uic_resolved)
        return state == "AutomatedTrading"

    def get_prices(self, asset_type: str, symbol: Optional[str] = None, uic: Optional[int] = None) -> dict:
        """Get current Ask/Bid prices for the instrument."""
        uic_resolved = self._resolve_uic(uic, symbol, asset_type)
        r = tr.infoprices.InfoPrices(Uic=uic_resolved, AssetType=asset_type)
        return self._api.request(r)

    # ---------------------------------------------------------
    # Order Execution (Write Operations)
    # ---------------------------------------------------------
    def market_order(
        self,
        asset_type: str,
        amount: int | float,
        symbol: Optional[str] = None,
        uic: Optional[int] = None,
        **kwargs,
    ) -> dict:
        """Place a Market Order."""
        uic_resolved = self._resolve_uic(uic, symbol, asset_type)
        order = MarketOrder(Uic=uic_resolved, Amount=amount, AssetType=asset_type, **kwargs)
        return self._execute_order(order)

    def limit_order(
        self,
        asset_type: str,
        amount: int | float,
        order_price: float,
        symbol: Optional[str] = None,
        uic: Optional[int] = None,
        **kwargs,
    ) -> dict:
        """Place a Limit Order."""
        uic_resolved = self._resolve_uic(uic, symbol, asset_type)
        order = LimitOrder(Uic=uic_resolved, Amount=amount, OrderPrice=order_price, AssetType=asset_type, **kwargs)
        return self._execute_order(order)

    def stop_order(
        self,
        asset_type: str,
        amount: int | float,
        order_price: float,
        symbol: Optional[str] = None,
        uic: Optional[int] = None,
        **kwargs,
    ) -> dict:
        """Place a Stop Order with Smart Routing."""
        uic_resolved = self._resolve_uic(uic, symbol, asset_type)
        details = self.get_instrument_details(asset_type=asset_type, uic=uic_resolved)
        supported_types = details.get("SupportedOrderTypes", [])

        if "Stop" in supported_types:
            order = StopOrder(Uic=uic_resolved, Amount=amount, OrderPrice=order_price, AssetType=asset_type, **kwargs)
        elif "StopIfTraded" in supported_types:
            order = StopIfTradedOrder(Uic=uic_resolved, Amount=amount, OrderPrice=order_price, AssetType=asset_type, **kwargs)
        else:
            order = StopOrder(Uic=uic_resolved, Amount=amount, OrderPrice=order_price, AssetType=asset_type, **kwargs)

        return self._execute_order(order)

    def cancel_order(self, order_id: str) -> dict:
        """Cancel an active order by ID."""
        r = tr.orders.CancelOrder(OrderId=order_id)
        return self._api.request(r)
