"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class CSVFileUploadForBulkBookingsRequest(_FlexModel):
    BookingReference: Optional[int] = Field(default=None, alias="BookingReference", description="Request reference id generated for the uploaded file to get the booking status.")

class GettheoverallstatusofbookingsuploadedviaCSVfileRequest(_FlexModel):
    RequestReferenceNumber: Optional[int] = Field(default=None, alias="RequestReferenceNumber", description="Booking request reference number.")

class GetdetailsvalidationstatusforbookingusingRequestReferenceNumberRequest(_FlexModel):
    RequestReferenceNumber: Optional[int] = Field(default=None, alias="RequestReferenceNumber", description="Booking request reference number.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
