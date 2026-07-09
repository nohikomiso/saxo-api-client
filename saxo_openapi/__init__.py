# サブモジュールをインポート
from . import contrib, endpoints
from .exceptions import OpenAPIError
from .saxo_openapi import API

# よく使われる定義（Enum）をトップレベルに露出
from .definitions.orders import AssetType, OrderType, OrderDurationType, Direction

# バージョン情報
__version__ = "0.1.0"

# APIを直接インポートできるようにする
__all__ = [
    "API",
    "OpenAPIError",
    "contrib",
    "endpoints",
    "AssetType",
    "OrderType",
    "OrderDurationType",
    "Direction"
]
