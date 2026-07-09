"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class SortByRule(_FlexModel):
    Ascending: Optional[Any] = Field(default=None, alias="Ascending", description="Sorting data in Ascending order.")
    Descending: Optional[Any] = Field(default=None, alias="Descending", description="Sorting data in Descending order.")

class GetAccountstatementreportfortheaccountsofaSpecifiedclientRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The account group id.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account key.")
    AccountStatementSortByRule: Optional[SortByRule] = Field(default=None, alias="AccountStatementSortByRule", description="Sorting Account statement data order by account statement id.By default, it sorts in Descending order.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique id of the client.")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="Include Account statement from this date. By default returns the previous date report.")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="Include Account statement till this date. By default returns the previous date report.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
