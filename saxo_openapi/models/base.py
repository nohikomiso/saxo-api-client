"""
Saxo OpenAPI Pydantic Models - Base definitions.
"""
from pydantic import BaseModel, ConfigDict


class _FlexModel(BaseModel):
    """
    Saxo API レスポンス解析用の柔軟なPydantic基底モデル。

    SaxoBankのAPIレスポンスは、エンドポイントのパラメータ（FieldGroups等）や
    AssetType によって、返却されるフィールドが動的に増減します。
    また将来的なAPI拡張により未知のフィールドが追加される可能性があります。

    このモデルは `extra="allow"` を設定することで、未知のフィールドによる
    パースエラー（ValidationError）を防ぎ、堅牢な正規化を実現します。
    """
    model_config = ConfigDict(extra="allow")

