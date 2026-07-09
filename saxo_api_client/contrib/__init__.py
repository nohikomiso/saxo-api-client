"""
Contrib module - high-level helper classes for trading.

These classes are NOT imported at package level to avoid circular imports.
Import directly from submodules:

    from saxo_api_client.contrib.client import SaxoClient
    from saxo_api_client.contrib.option_trader import OptionTrader
    from saxo_api_client.contrib.option_finder import OptionFinder
    from saxo_api_client.contrib.session import account_info
"""

# 循環インポートを避けるため、トップレベルではインポートしない
# 必要な場合は各サブモジュールから直接インポートすること

__all__ = [
    "session",
    "client",
    "orders",
    "option_finder",
    "option_trader",
    "option_types",
]
