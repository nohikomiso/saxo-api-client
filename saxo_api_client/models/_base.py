from pydantic import BaseModel, ConfigDict

class _FlexModel(BaseModel):
    """
    SaxoBank OpenAPI のための基礎モデル (Layer 1)。
    SaxoBank の仕様は非常に複雑であり、ドキュメントに記載のないキーが返ってきたり、
    必須とされている項目が実際には不要であったりするケースが多発します。
    そのため、すべてのモデルはこの `_FlexModel` を継承し、以下の設定を強制します：
    1. extra='allow': 未知のフィールドがJSONに含まれていてもエラーにせず保持する。
    2. 全フィールドが Optional (生成時に強制済み): クライアント側でのパースエラーを防止する。
    """
    model_config = ConfigDict(
        extra='allow',
        populate_by_name=True,
    )
