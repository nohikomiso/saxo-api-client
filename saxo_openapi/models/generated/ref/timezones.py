"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class TimeZoneDetails(_FlexModel):
    DisplayName: Optional[str] = Field(default=None, alias="DisplayName", description="Full name/description of the time zone.")
    TimeZoneAbbreviation: Optional[str] = Field(default=None, alias="TimeZoneAbbreviation", description="Time Zone Abbreviation for UTC standard time")
    TimeZoneId: Optional[str] = Field(default=None, alias="TimeZoneId", description="Internal unique time zone identifier.")
    TimeZoneOffset: Optional[str] = Field(default=None, alias="TimeZoneOffset", description="Time Zone Offset")
    ZoneName: Optional[str] = Field(default=None, alias="ZoneName", description="The IANA/tz database time zone identifier.")

class GetalistofalltimezonesRequest(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[TimeZoneDetails]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
