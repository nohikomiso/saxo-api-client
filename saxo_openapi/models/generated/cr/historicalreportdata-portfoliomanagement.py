"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class OptionalReportSection(_FlexModel):
    Transactions: Optional[Any] = Field(default=None, alias="Transactions", description="Add transaction section")

class GetPortfolioreportfortheaccountsofaspecifiedclientRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The account group id.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account key.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique id of the client.")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="From date in UTC")
    IncludeYTDInformation: Optional[bool] = Field(default=None, alias="IncludeYTDInformation", description="Include additional information about performance Year To Date.")
    IsSdcCLient: Optional[bool] = Field(default=None, alias="IsSdcCLient", description="")
    OptionalReportSections: Optional[List[OptionalReportSection]] = Field(default=None, alias="OptionalReportSections", description="Whether any optional section is needed in the report")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="To date in UTC")

class missingtitleRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="")
    FromDate: Optional[str] = Field(default=None, alias="FromDate", description="")
    IncludeYTDInformation: Optional[bool] = Field(default=None, alias="IncludeYTDInformation", description="")
    OptionalReportSections: Optional[List[OptionalReportSection]] = Field(default=None, alias="OptionalReportSections", description="")
    ToDate: Optional[str] = Field(default=None, alias="ToDate", description="")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
