"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class MyInforedirectendpointtoupdateverificationstatusMyInforedirectsonthisendpointoncetheinteractiveverificationiscompleteRequest(_FlexModel):
    Code: Optional[str] = Field(default=None, alias="Code", description="Verification code that will be used to fetch result from MyInfo")
    State: Optional[str] = Field(default=None, alias="State", description="State returned by MyInfo. It is the same state which was sent in the start verification request to MyInfo")

class CallbackendpointtoupdateverificationstatussigncatredirectsonthisendpointonceinteractiveverificationgetcompletedRequest(_FlexModel):
    Correlationid: Optional[str] = Field(default=None, alias="Correlationid", description="")
    Key: Optional[str] = Field(default=None, alias="Key", description="")
    Value: Optional[str] = Field(default=None, alias="Value", description="")

class RedirectendpointtoupdateverificationstatussigncatredirectsonthisendpointonceOidcinteractiveverificationgetcompletedThiswillbeusedforverificationviaMITIDRequest(_FlexModel):
    Code: Optional[str] = Field(default=None, alias="Code", description="This is OIDC authorisation code send after verification is completed. This will be used to get auth token to fetch client information")
    Error: Optional[str] = Field(default=None, alias="Error", description="Error code returned from Signicat")
    Error_Description: Optional[str] = Field(default=None, alias="Error_Description", description="Error description returned from Signicat")
    Method: Optional[str] = Field(default=None, alias="Method", description="")
    State: Optional[str] = Field(default=None, alias="State", description="State sent in redirect URL. This will be used to validate authenticity of redirecton")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
