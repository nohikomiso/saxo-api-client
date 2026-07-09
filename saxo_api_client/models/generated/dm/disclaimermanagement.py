"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetdisclaimerswithgivendisclaimertokensRequest(_FlexModel):
    DisclaimerTokens: Optional[List[str]] = Field(default=None, alias="DisclaimerTokens", description="disclaimer tokens")

class DisclaimerResponseType(_FlexModel):
    Accepted: Optional[Any] = Field(default=None, alias="Accepted", description="Disclaimer accepted")
    AlternateAccepted: Optional[Any] = Field(default=None, alias="AlternateAccepted", description="Disclaimer alternate accepted")
    Dismissed: Optional[Any] = Field(default=None, alias="Dismissed", description="Disclaimer dismissed")
    None_: Optional[Any] = Field(default=None, alias="None", description="")

class RegisterusersdisclaimerresponseuserinputdisclaimerfordisclaimertokenandcontexttokenRequest(_FlexModel):
    DisclaimerContext: Optional[str] = Field(default=None, alias="DisclaimerContext", description="Unique token representing the context in which the disclaimers are shown. This token is provided from the pre-check endpoint together with the list of DisclaimerTokens.")
    DisclaimerToken: Optional[str] = Field(default=None, alias="DisclaimerToken", description="Identifies a specific disclaimer token")
    ResponseType: Optional[DisclaimerResponseType] = Field(default=None, alias="ResponseType", description="ResponseType for the disclaimer")
    UserInput: Optional[str] = Field(default=None, alias="UserInput", description="Additional user input in disclaimer response")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
