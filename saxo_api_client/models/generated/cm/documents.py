"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class DocumentType(_FlexModel):
    ClassificationEvidence: Optional[Any] = Field(default=None, alias="ClassificationEvidence", description="Document provided as an evidence by client to support their Accredited Investor status")
    PensionTransferRequest: Optional[Any] = Field(default=None, alias="PensionTransferRequest", description="Document detailing Pension Transfer Request")
    PowerOfAttorney: Optional[Any] = Field(default=None, alias="PowerOfAttorney", description="Legal document mentioning the details of the acts that can be done on behalf of the principal (client)")
    TaxSavingAccount: Optional[Any] = Field(default=None, alias="TaxSavingAccount", description="Document detailing Tax Saving Account")
    TaxSavingAccountWithTransfer: Optional[Any] = Field(default=None, alias="TaxSavingAccountWithTransfer", description="Tax saving account with transfer")

class Document(_FlexModel):
    Data: Optional[str] = Field(default=None, alias="Data", description="Document data in Base64 encoded string")
    DocumentType: Optional[DocumentType] = Field(default=None, alias="DocumentType", description="Document type")
    FileName: Optional[str] = Field(default=None, alias="FileName", description="Document name with extension")

class UploaddocumentsRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="ClientKey of the user for which documents are to be uploaded")
    Documents: Optional[List[Document]] = Field(default=None, alias="Documents", description="Details of documents to be uploaded")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
