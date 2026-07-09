"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetTradesExecutedreportfortheaccountsofaspecifiedclientThisreportisavailableinthefollowingformatsPDFExcelTorequestaspecificformatpleasesettheAcceptheaderonyourrequesttooneofthefollowingForPDFapplicationpdfForExcelapplicationvndopenxmlformatsofficedocumentspreadsheetmlsheetRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The account group id.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account key.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique id of the client.")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="Include TradesExecuted from this date. By default returns the previous date report.")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="Include TradesExecuted till this date. By default returns the previous date report.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
