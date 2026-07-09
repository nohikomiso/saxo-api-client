"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class SignupFlowDocumentType(_FlexModel):
    AccountViewToIb: Optional[Any] = Field(default=None, alias="AccountViewToIb", description="Document detailing Introducing-Broker/Client details, authorization from client and Broker commission details")
    AnnualAccounts: Optional[Any] = Field(default=None, alias="AnnualAccounts", description="Annual Accounts")
    BankStatement: Optional[Any] = Field(default=None, alias="BankStatement", description="Bank Statement")
    CrsStatus: Optional[Any] = Field(default=None, alias="CrsStatus", description="CRS Status")
    EsaContract: Optional[Any] = Field(default=None, alias="EsaContract", description="Document detailing ESA Contract")
    FeePaymentAuthorization: Optional[Any] = Field(default=None, alias="FeePaymentAuthorization", description="Document detailing Fee Payment Authorization")
    GeneralBusinessTerms: Optional[Any] = Field(default=None, alias="GeneralBusinessTerms", description="Document explaining general business terms")
    NotarizedIdPassport: Optional[Any] = Field(default=None, alias="NotarizedIdPassport", description="NotarizedIdPassport")
    PensionTransferRequest: Optional[Any] = Field(default=None, alias="PensionTransferRequest", description="Document detailing Pension Transfer Request")
    PowerOfAttorney: Optional[Any] = Field(default=None, alias="PowerOfAttorney", description="Legal document mentioning the details of the acts that can be done on behalf of the principal (client)")
    PowerOfAttorneyToIb: Optional[Any] = Field(default=None, alias="PowerOfAttorneyToIb", description="Legal document mentioning the details of the acts that an IB can undertake on behalf of the principal (client)")
    ProofOfIdentity: Optional[Any] = Field(default=None, alias="ProofOfIdentity", description="Document to verify the identity of client")
    ProofOfResidency: Optional[Any] = Field(default=None, alias="ProofOfResidency", description="Document to verify the residency of client")
    SourceOfFundsDocument: Optional[Any] = Field(default=None, alias="SourceOfFundsDocument", description="Document detailing all the sources which client have for generating funds")
    TaxSavingAccount: Optional[Any] = Field(default=None, alias="TaxSavingAccount", description="Document detailing Tax Saving Account")
    TaxSavingAccountWithTransfer: Optional[Any] = Field(default=None, alias="TaxSavingAccountWithTransfer", description="Tax saving account with transfer")
    TermsAndConditions: Optional[Any] = Field(default=None, alias="TermsAndConditions", description="Document explaining terms and conditions")
    TermsAndConditionsAldersopsparingPrivate: Optional[Any] = Field(default=None, alias="TermsAndConditionsAldersopsparingPrivate", description="Document detailing Terms and Conditions Aldersopsparing Private")
    TermsAndConditionsKapitalPensionPrivate: Optional[Any] = Field(default=None, alias="TermsAndConditionsKapitalPensionPrivate", description="Document detailing Terms and Conditions Kapital Pension Private")
    TermsAndConditionsRatePensionPrivate: Optional[Any] = Field(default=None, alias="TermsAndConditionsRatePensionPrivate", description="Document detailing Terms and Conditions Rate Pension Private")
    UsTaxForm: Optional[Any] = Field(default=None, alias="UsTaxForm", description="US Tax Form")

class SignupDocument(_FlexModel):
    Data: Optional[str] = Field(default=None, alias="Data", description="Content or data of document in base64 format.")
    DocumentType: Optional[SignupFlowDocumentType] = Field(default=None, alias="DocumentType", description="Type of document")
    FileName: Optional[str] = Field(default=None, alias="FileName", description="Name of document")
    RenewalDate: Optional[Any] = Field(default=None, alias="RenewalDate", description="Expiration date of document")
    Title: Optional[str] = Field(default=None, alias="Title", description="Title of the document")

class AddmultiplefilestoasignupcaseRequest(_FlexModel):
    Documents: Optional[List[SignupDocument]] = Field(default=None, alias="Documents", description="An array of base64 encoded files, documenting the identity, residency etc of the applicant.")
    SignUpId: Optional[str] = Field(default=None, alias="SignUpId", description="Signup ID")

class ValuePairsParentChildProperty(_FlexModel):
    Key: Optional[str] = Field(default=None, alias="Key", description="Child Key")
    ParentKey: Optional[str] = Field(default=None, alias="ParentKey", description="Child Property Keys")
    Value: Optional[str] = Field(default=None, alias="Value", description="Parent Property Key")

class SignUpOption(_FlexModel):
    ParentPropertyName: Optional[str] = Field(default=None, alias="ParentPropertyName", description="Parent Propery Name")
    PropertyName: Optional[str] = Field(default=None, alias="PropertyName", description="Property name")
    ValuePairs: Optional[List[ValuePairsParentChildProperty]] = Field(default=None, alias="ValuePairs", description="Key and value pairs of the property values")

class GetallsignupoptionsRequest(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[SignUpOption]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")

class MyInfoRequest(_FlexModel):
    RedirectUrl: Optional[str] = Field(default=None, alias="RedirectUrl", description="Redirect url to which the user will be redirected after verification is done")

class SecureMeUploadOption(_FlexModel):
    Camera: Optional[Any] = Field(default=None, alias="Camera", description="Camera")
    File: Optional[Any] = Field(default=None, alias="File", description="File")

class SecureMeUploadOptions(_FlexModel):
    Back: Optional[SecureMeUploadOption] = Field(default=None, alias="Back", description="Back side document option")
    Front: Optional[SecureMeUploadOption] = Field(default=None, alias="Front", description="Front side document option")
    Selfie: Optional[SecureMeUploadOption] = Field(default=None, alias="Selfie", description="Selfie option")

class SecureMeRequest(_FlexModel):
    CountryCode: Optional[str] = Field(default=None, alias="CountryCode", description="Country ISO code (from Options)")
    ErrorRedirectUrl: Optional[str] = Field(default=None, alias="ErrorRedirectUrl", description="Error redirect url")
    ServiceLanguageCode: Optional[str] = Field(default=None, alias="ServiceLanguageCode", description="Service language ISO code (from Options)")
    SuccessRedirectUrl: Optional[str] = Field(default=None, alias="SuccessRedirectUrl", description="Success redirect url")
    UploadOptions: Optional[SecureMeUploadOptions] = Field(default=None, alias="UploadOptions", description="SecureMe upload options")

class VerificationProvider(_FlexModel):
    MyInfo: Optional[Any] = Field(default=None, alias="MyInfo", description="MyInfo")
    SecureMe: Optional[Any] = Field(default=None, alias="SecureMe", description="SecureMe")

class InitiateverificationprocessfromexternalvendorRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The client key")
    MyInfoRequest: Optional[MyInfoRequest] = Field(default=None, alias="MyInfoRequest", description="MyInfo Request")
    SecureMeRequest: Optional[SecureMeRequest] = Field(default=None, alias="SecureMeRequest", description="Secure Me Request")
    VerificationProviderType: Optional[VerificationProvider] = Field(default=None, alias="VerificationProviderType", description="Type of verification provider requested")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
