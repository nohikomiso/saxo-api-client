"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class CaseStatus(_FlexModel):
    Canceled: Optional[Any] = Field(default=None, alias="Canceled", description="Case is cancelled")
    ExternallyPending: Optional[Any] = Field(default=None, alias="ExternallyPending", description="Case is externally pending")
    InformationProvided: Optional[Any] = Field(default=None, alias="InformationProvided", description="Information is provided for the case")
    InProgress: Optional[Any] = Field(default=None, alias="InProgress", description="Case is in progress")
    InternallyPending: Optional[Any] = Field(default=None, alias="InternallyPending", description="Case is internally pending")
    InternallyPendingEscalated: Optional[Any] = Field(default=None, alias="InternallyPendingEscalated", description="Case is internally pending and is escalated")
    Merged: Optional[Any] = Field(default=None, alias="Merged", description="Case is merged")
    ProblemSolved: Optional[Any] = Field(default=None, alias="ProblemSolved", description="Problem solved")

class GetalistofallsupportcasesRequest(_FlexModel):
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    FromDateTime: Optional[Any] = Field(default=None, alias="FromDateTime", description="Includes cases with latest activity time greater than or equal to FromDateTime")
    Status: Optional[List[CaseStatus]] = Field(default=None, alias="Status", description="Status: If specified will only return entries with the specified case status")
    ToDateTime: Optional[Any] = Field(default=None, alias="ToDateTime", description="Includes cases with latest activity time less than or equal to ToDateTime")

class FacilitatesanIBtocreateanewcaseonbehalfofitsclientRequest(_FlexModel):
    CaseTitle: Optional[str] = Field(default=None, alias="CaseTitle", description="Title of the case")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Identifies the client for whom case has to be created")
    Description: Optional[str] = Field(default=None, alias="Description", description="Description of case")
    NotifyClient: Optional[bool] = Field(default=None, alias="NotifyClient", description="Whether to notify client")
    ShowInPortal: Optional[bool] = Field(default=None, alias="ShowInPortal", description="Indicates if this case is available in portal")

class GetaspecificsupportcaseRequest(_FlexModel):
    CaseId: Optional[str] = Field(default=None, alias="CaseId", description="The case ID")

class UpdateCaseStatus(_FlexModel):
    ExternallyPending: Optional[Any] = Field(default=None, alias="ExternallyPending", description="Case is externally pending")
    InProgress: Optional[Any] = Field(default=None, alias="InProgress", description="Case is in progress")
    InternallyPending: Optional[Any] = Field(default=None, alias="InternallyPending", description="Case is internally pending")

class CaseType(_FlexModel):
    Faq: Optional[Any] = Field(default=None, alias="Faq", description="Case is a faq")
    Problem: Optional[Any] = Field(default=None, alias="Problem", description="Case is a problem")
    Question: Optional[Any] = Field(default=None, alias="Question", description="Case is a question")
    Request: Optional[Any] = Field(default=None, alias="Request", description="Case is a request")

class UpdatesupportcaseRequest(_FlexModel):
    CaseId: Optional[str] = Field(default=None, alias="CaseId", description="The case ID")
    CaseStatus: Optional[UpdateCaseStatus] = Field(default=None, alias="CaseStatus", description="Status of case")
    CaseType: Optional[CaseType] = Field(default=None, alias="CaseType", description="Type of case")
    Description: Optional[str] = Field(default=None, alias="Description", description="Description of case")
    FollowUpDueDate: Optional[Any] = Field(default=None, alias="FollowUpDueDate", description="Follow up due date of case")
    HandledByPartner: Optional[bool] = Field(default=None, alias="HandledByPartner", description="Represents if the case is handled by partner")
    IsEscalated: Optional[bool] = Field(default=None, alias="IsEscalated", description="Represents if the case is escalated")
    ShowInPortal: Optional[bool] = Field(default=None, alias="ShowInPortal", description="Represents if the case should be shown in portal")
    Title: Optional[str] = Field(default=None, alias="Title", description="Title of case")

class CloseCaseStatus(_FlexModel):
    Canceled: Optional[Any] = Field(default=None, alias="Canceled", description="Case is cancelled")
    InformationProvided: Optional[Any] = Field(default=None, alias="InformationProvided", description="Information is provided for the case")
    ProblemSolved: Optional[Any] = Field(default=None, alias="ProblemSolved", description="Problem solved")

class CloseaspecificsupportcaseRequest(_FlexModel):
    CaseId: Optional[str] = Field(default=None, alias="CaseId", description="The case ID")
    Status: Optional[CloseCaseStatus] = Field(default=None, alias="Status", description="Case Status")

class CreateinternalcommentunderacaseRequest(_FlexModel):
    CaseId: Optional[str] = Field(default=None, alias="CaseId", description="The case ID")
    Comment: Optional[str] = Field(default=None, alias="Comment", description="Internal Comment")

class File(_FlexModel):
    Data: Optional[str] = Field(default=None, alias="Data", description="Content or data of document in base64 format.")
    FileName: Optional[str] = Field(default=None, alias="FileName", description="File name poa.pdf")
    MimeType: Optional[str] = Field(default=None, alias="MimeType", description="Mime type")

class CreatenoteunderacaseRequest(_FlexModel):
    Attachment: Optional[File] = Field(default=None, alias="Attachment", description="Attachment of note")
    CaseId: Optional[str] = Field(default=None, alias="CaseId", description="The case ID")
    Note: Optional[str] = Field(default=None, alias="Note", description="Note")
    Title: Optional[str] = Field(default=None, alias="Title", description="Title of note")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
