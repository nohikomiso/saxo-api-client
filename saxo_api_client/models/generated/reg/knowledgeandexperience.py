"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class RegulatoryContext(_FlexModel):
    Advisory: Optional[Any] = Field(default=None, alias="Advisory", description="Test has been taken as part of an advisory session")

class RetrievethelatestappropriatenessstatusRequest(_FlexModel):
    RegulatoryContext: Optional[RegulatoryContext] = Field(default=None, alias="RegulatoryContext", description="")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="")

class GetquestionsandresponsesrelatedtothegeneralKnowledgeandExperienceassessmentRequest(_FlexModel):
    RegulatoryContext: Optional[RegulatoryContext] = Field(default=None, alias="RegulatoryContext", description="")
    SectionName: Optional[str] = Field(default=None, alias="SectionName", description="Name of the section.")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
