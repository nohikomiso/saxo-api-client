"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetRenewalDataforthepassedClientUserorloggedinuserPriorityisgiventouserKeyoverclientKeyRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="ClientKey of the primary user for which renewal is requested")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="UserKey of the user for which renewal is requested")

class RenewalDocumentType(_FlexModel):
    AccountViewToIb: Optional[Any] = Field(default=None, alias="AccountViewToIb", description="Account view to IB.")
    AmlScreening: Optional[Any] = Field(default=None, alias="AmlScreening", description="Aml screening document")
    AnnualAccounts: Optional[Any] = Field(default=None, alias="AnnualAccounts", description="Annual Accounts")
    ArticlesMemorandum: Optional[Any] = Field(default=None, alias="ArticlesMemorandum", description="Articles Memorandum")
    AuthorizedDealers: Optional[Any] = Field(default=None, alias="AuthorizedDealers", description="Authorized Dealers")
    AuthorizedPaymentSignatories: Optional[Any] = Field(default=None, alias="AuthorizedPaymentSignatories", description="Authorized Payment Signatories")
    BackOfficeReporting: Optional[Any] = Field(default=None, alias="BackOfficeReporting", description="Back Office Reporting")
    BankStatement: Optional[Any] = Field(default=None, alias="BankStatement", description="Bank Statement")
    BeneficialOwnerInformation: Optional[Any] = Field(default=None, alias="BeneficialOwnerInformation", description="Beneficial Owner Information")
    CertificateOfGoodStanding: Optional[Any] = Field(default=None, alias="CertificateOfGoodStanding", description="Certificate Of Good Standing")
    CertificateOfIncorporation: Optional[Any] = Field(default=None, alias="CertificateOfIncorporation", description="Certificate Of Incorporation")
    CertificateOfIncumbency: Optional[Any] = Field(default=None, alias="CertificateOfIncumbency", description="Certificate Of Incumbency")
    CertificateOfSignature: Optional[Any] = Field(default=None, alias="CertificateOfSignature", description="Certificate Of Signature")
    ClassificationEvidence: Optional[Any] = Field(default=None, alias="ClassificationEvidence", description="Classification Evidence")
    ClientApplicationForm: Optional[Any] = Field(default=None, alias="ClientApplicationForm", description="Client application form document")
    CorporateDisclosureForm: Optional[Any] = Field(default=None, alias="CorporateDisclosureForm", description="Corporate Disclosure Form")
    CorporateTranscript: Optional[Any] = Field(default=None, alias="CorporateTranscript", description="Corporate Transcript")
    CRSStatus: Optional[Any] = Field(default=None, alias="CRSStatus", description="CRS Status")
    DdNotesFromClient: Optional[Any] = Field(default=None, alias="DdNotesFromClient", description="Dd Notes From Client")
    DirectorSignatoryInformation: Optional[Any] = Field(default=None, alias="DirectorSignatoryInformation", description="Director Signatory Information")
    ElectonicIdVerification: Optional[Any] = Field(default=None, alias="ElectonicIdVerification", description="Electonic Id Verification")
    EsaContract: Optional[Any] = Field(default=None, alias="EsaContract", description="Esa Contract")
    EsmaDocumentation: Optional[Any] = Field(default=None, alias="EsmaDocumentation", description="Esma Documentation")
    FeePaymentAuthorization: Optional[Any] = Field(default=None, alias="FeePaymentAuthorization", description="Fee Payment Authorization")
    FeePaymentSchedule: Optional[Any] = Field(default=None, alias="FeePaymentSchedule", description="Fee Payment Schedule")
    GeneralBusinessTerms: Optional[Any] = Field(default=None, alias="GeneralBusinessTerms", description="General business terms.")
    IbAddendumScml: Optional[Any] = Field(default=None, alias="IbAddendumScml", description="Ib Addendum Scml")
    InternalTranslationForm: Optional[Any] = Field(default=None, alias="InternalTranslationForm", description="Internal Translation Form")
    ItalianAccountOpeningConfirmation: Optional[Any] = Field(default=None, alias="ItalianAccountOpeningConfirmation", description="Italian Account Opening Confirmation")
    JointAccountForm: Optional[Any] = Field(default=None, alias="JointAccountForm", description="Joint Account Form")
    LanguageLegalLetter: Optional[Any] = Field(default=None, alias="LanguageLegalLetter", description="Language Legal Letter")
    LawyersLicense: Optional[Any] = Field(default=None, alias="LawyersLicense", description="Lawyers License")
    MifidClassification: Optional[Any] = Field(default=None, alias="MifidClassification", description="Mifid Classification")
    MultipleAccountForm: Optional[Any] = Field(default=None, alias="MultipleAccountForm", description="Multiple Account Form")
    OtherDdDocs: Optional[Any] = Field(default=None, alias="OtherDdDocs", description="Other Dd Docs")
    PensionTransferRequest: Optional[Any] = Field(default=None, alias="PensionTransferRequest", description="Pension Transfer Request")
    PoaAuthTrade: Optional[Any] = Field(default=None, alias="PoaAuthTrade", description="Poa Auth Trade")
    PoaF07: Optional[Any] = Field(default=None, alias="PoaF07", description="PoaF07")
    PoaFp2: Optional[Any] = Field(default=None, alias="PoaFp2", description="PoaFp2")
    PoaI07: Optional[Any] = Field(default=None, alias="PoaI07", description="PoaI07")
    PoaI08: Optional[Any] = Field(default=None, alias="PoaI08", description="PoaI08")
    PoaIblp4: Optional[Any] = Field(default=None, alias="PoaIblp4", description="PoaIblp4")
    PoaIbp5: Optional[Any] = Field(default=None, alias="PoaIbp5", description="PoaIbp5")
    PoaIpb6: Optional[Any] = Field(default=None, alias="PoaIpb6", description="PoaIpb6")
    PoaLp1: Optional[Any] = Field(default=None, alias="PoaLp1", description="PoaLp1")
    PoaMa10: Optional[Any] = Field(default=None, alias="PoaMa10", description="PoaMa10")
    PoaMa11: Optional[Any] = Field(default=None, alias="PoaMa11", description="PoaMa11")
    PoaMm9: Optional[Any] = Field(default=None, alias="PoaMm9", description="PoaMm9")
    PowerOfAttorney: Optional[Any] = Field(default=None, alias="PowerOfAttorney", description="Power of attorney.")
    PowerOfAttorneyToIb: Optional[Any] = Field(default=None, alias="PowerOfAttorneyToIb", description="Power of Attorney to Ib")
    PowerOfAttorneyToPerformanceIb: Optional[Any] = Field(default=None, alias="PowerOfAttorneyToPerformanceIb", description="Power of attorney to performance Ib")
    ProofOfIdentity: Optional[Any] = Field(default=None, alias="ProofOfIdentity", description="Proof of identity.")
    ProofOfResidency: Optional[Any] = Field(default=None, alias="ProofOfResidency", description="Proof of residence.")
    Selfie: Optional[Any] = Field(default=None, alias="Selfie", description="Selfie of the client")
    ShareCertification: Optional[Any] = Field(default=None, alias="ShareCertification", description="Share Certification")
    SourceOfFundsDocument: Optional[Any] = Field(default=None, alias="SourceOfFundsDocument", description="Source of funds document.")
    TaxDocumentation: Optional[Any] = Field(default=None, alias="TaxDocumentation", description="Tax Documentation")
    TaxLiability: Optional[Any] = Field(default=None, alias="TaxLiability", description="Tax Liability")
    TaxReclaimRegistrationForms: Optional[Any] = Field(default=None, alias="TaxReclaimRegistrationForms", description="Tax Reclaim Registration Forms")
    TermsAndConditions: Optional[Any] = Field(default=None, alias="TermsAndConditions", description="Terms and conditions.")
    TermsAndConditionsAldersopsparingPrivate: Optional[Any] = Field(default=None, alias="TermsAndConditionsAldersopsparingPrivate", description="Terms And Conditions Aldersopsparing Private")
    TermsAndConditionsKapitalPensionPrivate: Optional[Any] = Field(default=None, alias="TermsAndConditionsKapitalPensionPrivate", description="Terms And Conditions Kapital Pension Private")
    TermsAndConditionsRatePensionEmployer: Optional[Any] = Field(default=None, alias="TermsAndConditionsRatePensionEmployer", description="Terms And Conditions Rate Pension Employer")
    TermsAndConditionsRatePensionPrivate: Optional[Any] = Field(default=None, alias="TermsAndConditionsRatePensionPrivate", description="Terms And Conditions Rate Pension Private")
    W8Ben: Optional[Any] = Field(default=None, alias="W8Ben", description="W8Ben")

class RenewalDocument(_FlexModel):
    Data: Optional[str] = Field(default=None, alias="Data", description="Base64 encoded document data")
    MimeType: Optional[str] = Field(default=None, alias="MimeType", description="Mime type of the document")
    Name: Optional[str] = Field(default=None, alias="Name", description="Document name")
    Type: Optional[RenewalDocumentType] = Field(default=None, alias="Type", description="Renewal document type")

class AustraliaData(_FlexModel):
    AnnualIncome: Optional[str] = Field(default=None, alias="AnnualIncome", description="Annual Income in AUD")
    NetWorth: Optional[str] = Field(default=None, alias="NetWorth", description="Net Worth in AUD")

class FinlandData(_FlexModel):
    EuroClearSectorCode: Optional[str] = Field(default=None, alias="EuroClearSectorCode", description="Sector code for Euroclear")

class AmountDescriptionType(_FlexModel):
    AboveThisAmount: Optional[Any] = Field(default=None, alias="AboveThisAmount", description="Value is above this amount.")
    Exact: Optional[Any] = Field(default=None, alias="Exact", description="Exact value provided.")
    Rounded: Optional[Any] = Field(default=None, alias="Rounded", description="Nearby value provided.")

class AssetDetails(_FlexModel):
    Amount: Optional[int] = Field(default=None, alias="Amount", description="Amount value")
    AmountDescription: Optional[AmountDescriptionType] = Field(default=None, alias="AmountDescription", description="Amount Description")
    CurrencyCode: Optional[str] = Field(default=None, alias="CurrencyCode", description="Currency code (from Options)")

class GlobalFinancialInformation(_FlexModel):
    AnnualIncomeAfterTax: Optional[AssetDetails] = Field(default=None, alias="AnnualIncomeAfterTax", description="Annual Income After Tax")
    IntendToInvest: Optional[AssetDetails] = Field(default=None, alias="IntendToInvest", description="Intend To Invest")
    InvestableAsset: Optional[AssetDetails] = Field(default=None, alias="InvestableAsset", description="Investable Asset")

class HongkongData(_FlexModel):
    NetWorthInUsd: Optional[str] = Field(default=None, alias="NetWorthInUsd", description="Net worth in USD")
    TotalEstimatedAnnualIncomeInUsd: Optional[str] = Field(default=None, alias="TotalEstimatedAnnualIncomeInUsd", description="Estimated annual income in USD")

class EmploymentInformation(_FlexModel):
    CountryConcernedCode: Optional[str] = Field(default=None, alias="CountryConcernedCode", description="Concerned country code")
    DetailedBusinessActivity: Optional[str] = Field(default=None, alias="DetailedBusinessActivity", description="Business activityin detail")
    OtherEmployment: Optional[str] = Field(default=None, alias="OtherEmployment", description="Name of the other employment")
    ProvinceConcerned: Optional[str] = Field(default=None, alias="ProvinceConcerned", description="Concerned province")
    StatusOfEmployment: Optional[str] = Field(default=None, alias="StatusOfEmployment", description="Status of employment")

class AnnualIncomeInformation(_FlexModel):
    AnnualIncomeSource: Optional[List[str]] = Field(default=None, alias="AnnualIncomeSource", description="Annual income source - (from options, can select multiple)")
    TotalAnnualIncome: Optional[str] = Field(default=None, alias="TotalAnnualIncome", description="Total annual income - (from options)")

class InvestableAssets(_FlexModel):
    NatureAndPurposeOfTheRelationship: Optional[str] = Field(default=None, alias="NatureAndPurposeOfTheRelationship", description="Nature and purpose of relationship - (from options)")
    SourceOfWealth: Optional[List[str]] = Field(default=None, alias="SourceOfWealth", description="Sources of wealth - (from options, can select multiple)")
    ValueOfTotalWealth: Optional[str] = Field(default=None, alias="ValueOfTotalWealth", description="Value of total wealth - (from options)")

class ProfileInformation(_FlexModel):
    AnnualIncomeInformation: Optional[AnnualIncomeInformation] = Field(default=None, alias="AnnualIncomeInformation", description="Annual income information for Italy")
    InvestableAssets: Optional[InvestableAssets] = Field(default=None, alias="InvestableAssets", description="Investable assets for Italy")

class ItalyData(_FlexModel):
    EmploymentInformation: Optional[EmploymentInformation] = Field(default=None, alias="EmploymentInformation", description="Employment information for Italy renewal")
    MailContactPreference: Optional[bool] = Field(default=None, alias="MailContactPreference", description="Do you want to be contacted through mail?")
    ProfileInformation: Optional[ProfileInformation] = Field(default=None, alias="ProfileInformation", description="Profile information for Italy renewal")

class JapanData(_FlexModel):
    AnnualIncomeJpy: Optional[str] = Field(default=None, alias="AnnualIncomeJpy", description="Annual Income (in 10 000 JPY)")
    NetWorthJpy: Optional[str] = Field(default=None, alias="NetWorthJpy", description="Net Worth (in 10 000 JPY)")
    TickerCodes: Optional[List[str]] = Field(default=None, alias="TickerCodes", description="Ticker codes")

class AdditionalNationality(_FlexModel):
    CountryCode: Optional[str] = Field(default=None, alias="CountryCode", description="Additional country (from Options)")
    NationalId: Optional[str] = Field(default=None, alias="NationalId", description="Additional national id")
    NationalIdType: Optional[int] = Field(default=None, alias="NationalIdType", description="Additional national id type")

class TaxableCountry(_FlexModel):
    CountryCode: Optional[str] = Field(default=None, alias="CountryCode", description="Country code (from Options)")
    TaxId: Optional[str] = Field(default=None, alias="TaxId", description="Tax Id, if TIN is available")
    TinMissingReason: Optional[str] = Field(default=None, alias="TinMissingReason", description="Reason for not having TIN (from Options)")
    TinNotAvailable: Optional[bool] = Field(default=None, alias="TinNotAvailable", description="Is TIN not available?")
    TinOtherMissingReason: Optional[str] = Field(default=None, alias="TinOtherMissingReason", description="Any other reason for not having TIN")

class PhoneNumber(_FlexModel):
    CountryCode: Optional[str] = Field(default=None, alias="CountryCode", description="Country Code (from Options)")
    Number: Optional[str] = Field(default=None, alias="Number", description="Number")

class ContactInformation(_FlexModel):
    EmailAddress: Optional[str] = Field(default=None, alias="EmailAddress", description="Email Address")
    MobileNumber: Optional[PhoneNumber] = Field(default=None, alias="MobileNumber", description="Mobile Number")
    PrimaryPhoneNumber: Optional[PhoneNumber] = Field(default=None, alias="PrimaryPhoneNumber", description="Primary PhoneNumber")
    SecondaryPhoneNumber: Optional[PhoneNumber] = Field(default=None, alias="SecondaryPhoneNumber", description="Secondary PhoneNumber")

class MinorLegalGuardianship(_FlexModel):
    Other: Optional[Any] = Field(default=None, alias="Other", description="Other status")
    Sharedwithanotherlegalguardian: Optional[Any] = Field(default=None, alias="Sharedwithanotherlegalguardian", description="Shared with another legal guarduan")
    Single: Optional[Any] = Field(default=None, alias="Single", description="Single guardian")

class MinorInformation(_FlexModel):
    MinorLegalGuardianship: Optional[MinorLegalGuardianship] = Field(default=None, alias="MinorLegalGuardianship", description="Minor legal guardianship type")
    OtherReason: Optional[str] = Field(default=None, alias="OtherReason", description="Reason for setting other legal guardianship")
    SharedResponsibilityWithLegalGuardian: Optional[str] = Field(default=None, alias="SharedResponsibilityWithLegalGuardian", description="Id of the shared legal guardian(ReadOnly)")
    SharedResponsibilityWithLegalGuardianLoginUserId: Optional[str] = Field(default=None, alias="SharedResponsibilityWithLegalGuardianLoginUserId", description="Login userId of shared legal guardian")
    SharedResponsibilityWithLegalGuardianName: Optional[str] = Field(default=None, alias="SharedResponsibilityWithLegalGuardianName", description="Name of the shared legal guardian(ReadOnly)")

class NinMissingReason(_FlexModel):
    ExpiredinRenewal: Optional[Any] = Field(default=None, alias="ExpiredinRenewal", description="ExpiredinRenewal")
    FBLCollection: Optional[Any] = Field(default=None, alias="FBLCollection", description="FBLCollection")
    NotObtained: Optional[Any] = Field(default=None, alias="NotObtained", description="NotObtained")
    NotRequired: Optional[Any] = Field(default=None, alias="NotRequired", description="NotRequired")
    ODDCollection: Optional[Any] = Field(default=None, alias="ODDCollection", description="ODDCollection")
    Other: Optional[Any] = Field(default=None, alias="Other", description="Other")
    WrongFormat: Optional[Any] = Field(default=None, alias="WrongFormat", description="WrongFormat")

class NinMissingType(_FlexModel):
    NationalIdentityCard: Optional[Any] = Field(default=None, alias="NationalIdentityCard", description="NationalIdentityCard")
    Passport: Optional[Any] = Field(default=None, alias="Passport", description="Passport")
    TaxID: Optional[Any] = Field(default=None, alias="TaxID", description="TaxID")

class OnboardingAddress(_FlexModel):
    BuildingName: Optional[str] = Field(default=None, alias="BuildingName", description="Name of Building")
    BuildingNumber: Optional[str] = Field(default=None, alias="BuildingNumber", description="Building Number")
    City: Optional[str] = Field(default=None, alias="City", description="City")
    CoName: Optional[str] = Field(default=None, alias="CoName", description="Care of Name")
    CountryOfResidenceCode: Optional[str] = Field(default=None, alias="CountryOfResidenceCode", description="Country of residence ISO code (from Options)")
    Floor: Optional[str] = Field(default=None, alias="Floor", description="Floor")
    LocalArea: Optional[str] = Field(default=None, alias="LocalArea", description="Local area")
    PostalCode: Optional[str] = Field(default=None, alias="PostalCode", description="PostalCode")
    PostBoxOffice: Optional[str] = Field(default=None, alias="PostBoxOffice", description="Post box office")
    SideDoor: Optional[str] = Field(default=None, alias="SideDoor", description="Side door")
    State: Optional[str] = Field(default=None, alias="State", description="State")
    StreetName: Optional[str] = Field(default=None, alias="StreetName", description="Name of Street")
    Unit: Optional[str] = Field(default=None, alias="Unit", description="Unit")

class PoliticallyExposedInformation(_FlexModel):
    PepPosition: Optional[str] = Field(default=None, alias="PepPosition", description="PEP Position")
    PepRelatedPersonName: Optional[str] = Field(default=None, alias="PepRelatedPersonName", description="Name of PEP Related Person")
    PepRelatedPersonPosition: Optional[str] = Field(default=None, alias="PepRelatedPersonPosition", description="Position of PEP Related Person")
    PepType: Optional[str] = Field(default=None, alias="PepType", description="Type of PEP (from Options)")
    RelationToPep: Optional[str] = Field(default=None, alias="RelationToPep", description="Relation to PEP (from Options)")

class PersonalInformation(_FlexModel):
    AdditionalNationalities: Optional[List[AdditionalNationality]] = Field(default=None, alias="AdditionalNationalities", description="Additional nationalities")
    AdditionalTaxableCountries: Optional[List[TaxableCountry]] = Field(default=None, alias="AdditionalTaxableCountries", description="Additional taxable countries")
    AliasFirstName: Optional[str] = Field(default=None, alias="AliasFirstName", description="Alias first name")
    AliasLastName: Optional[str] = Field(default=None, alias="AliasLastName", description="Alias last name")
    CityOfBirth: Optional[str] = Field(default=None, alias="CityOfBirth", description="City Of Birth")
    ContactInformation: Optional[ContactInformation] = Field(default=None, alias="ContactInformation", description="Contact Details")
    CountryOfBirth: Optional[str] = Field(default=None, alias="CountryOfBirth", description="Country Of Birth (from Options)")
    DateOfBirth: Optional[str] = Field(default=None, alias="DateOfBirth", description="DateOfBirth")
    EmploymentInformation: Optional[EmploymentInformation] = Field(default=None, alias="EmploymentInformation", description="Employment Details")
    FirstName: Optional[str] = Field(default=None, alias="FirstName", description="First Name")
    Gender: Optional[str] = Field(default=None, alias="Gender", description="Gender (from Options)")
    LastName: Optional[str] = Field(default=None, alias="LastName", description="Last Name")
    MinorInformation: Optional[MinorInformation] = Field(default=None, alias="MinorInformation", description="Legal guardian of minor customer")
    NationalityCode: Optional[str] = Field(default=None, alias="NationalityCode", description="Nationality Code (from Options)")
    NinMissingReason: Optional[NinMissingReason] = Field(default=None, alias="NinMissingReason", description="NinMissingReason")
    NinMissingType: Optional[NinMissingType] = Field(default=None, alias="NinMissingType", description="NinMissingType")
    NinNotAvailable: Optional[bool] = Field(default=None, alias="NinNotAvailable", description="NinNotAvailable")
    OriginalScriptFirstName: Optional[str] = Field(default=None, alias="OriginalScriptFirstName", description="Original script first name")
    OriginalScriptLastName: Optional[str] = Field(default=None, alias="OriginalScriptLastName", description="Original script last name")
    OtherAddress: Optional[OnboardingAddress] = Field(default=None, alias="OtherAddress", description="Other address")
    PermanentResidency: Optional[str] = Field(default=None, alias="PermanentResidency", description="Permanent Residency")
    PersonalId: Optional[str] = Field(default=None, alias="PersonalId", description="Personal Id")
    PersonalIdExpirationDate: Optional[str] = Field(default=None, alias="PersonalIdExpirationDate", description="Personal id expiration date")
    PersonalIdPlaceOfRelease: Optional[str] = Field(default=None, alias="PersonalIdPlaceOfRelease", description="Place of release of personal ID")
    PersonalIdReleaseDate: Optional[str] = Field(default=None, alias="PersonalIdReleaseDate", description="Release date of personal ID")
    PersonalIdReleasedBy: Optional[str] = Field(default=None, alias="PersonalIdReleasedBy", description="Personal ID released by")
    PersonalIdType: Optional[str] = Field(default=None, alias="PersonalIdType", description="Personal ID Type (from Options)")
    PoiExpirationDate: Optional[str] = Field(default=None, alias="PoiExpirationDate", description="POI Expiration Date")
    PoliticallyExposedInformation: Optional[PoliticallyExposedInformation] = Field(default=None, alias="PoliticallyExposedInformation", description="Politically exposed person information")
    PoliticallyExposedPerson: Optional[bool] = Field(default=None, alias="PoliticallyExposedPerson", description="Politically Exposed Person")
    ResidentialAddress: Optional[OnboardingAddress] = Field(default=None, alias="ResidentialAddress", description="Residential Address")
    TaxId: Optional[str] = Field(default=None, alias="TaxId", description="Tax Id")
    TinMissingReason: Optional[str] = Field(default=None, alias="TinMissingReason", description="Reason for not having TIN (from Options)")
    TinNotAvailable: Optional[bool] = Field(default=None, alias="TinNotAvailable", description="Tin Not Available")
    TinOtherMissingReason: Optional[str] = Field(default=None, alias="TinOtherMissingReason", description="Any other reason for not having TIN")

class FatcaDeclaration(_FlexModel):
    UnitedStatesCitizen: Optional[bool] = Field(default=None, alias="UnitedStatesCitizen", description="United States Citizen")
    UnitedStatesTaxId: Optional[str] = Field(default=None, alias="UnitedStatesTaxId", description="United States TaxId")
    UnitedStatesTaxLiable: Optional[bool] = Field(default=None, alias="UnitedStatesTaxLiable", description="United States Tax Liable")

class RegulatoryInformation(_FlexModel):
    FatcaDeclaration: Optional[FatcaDeclaration] = Field(default=None, alias="FatcaDeclaration", description="Fatca Declaration")

class RelationshipStatus(_FlexModel):
    Invalid: Optional[Any] = Field(default=None, alias="Invalid", description="Invalid Relationship")
    Valid: Optional[Any] = Field(default=None, alias="Valid", description="Valid Relationship")

class CustomerRelationshipType(_FlexModel):
    JAHolder: Optional[Any] = Field(default=None, alias="JAHolder", description="Joint Account Holder")
    POAHolder: Optional[Any] = Field(default=None, alias="POAHolder", description="POA Holder")

class ConnectionType(_FlexModel):
    AuthorizedSignatory: Optional[Any] = Field(default=None, alias="AuthorizedSignatory", description="Authorized Signatory")
    BeneficialOwner: Optional[Any] = Field(default=None, alias="BeneficialOwner", description="Beneficial Owner")
    ConcubinageCivilPartnership: Optional[Any] = Field(default=None, alias="ConcubinageCivilPartnership", description="Concubinage Civil Partnership")
    Director: Optional[Any] = Field(default=None, alias="Director", description="Director")
    ExtendedFamily: Optional[Any] = Field(default=None, alias="ExtendedFamily", description="Extended Family")
    LegalGuardianBeneficialOwner: Optional[Any] = Field(default=None, alias="LegalGuardianBeneficialOwner", description="Legal Guardian Beneficial Owner")
    Other: Optional[Any] = Field(default=None, alias="Other", description="Other")
    ParentChild: Optional[Any] = Field(default=None, alias="ParentChild", description="Parent-Child")
    Sibling: Optional[Any] = Field(default=None, alias="Sibling", description="Sibling")
    Spouse: Optional[Any] = Field(default=None, alias="Spouse", description="Spouse")
    UnknownRelation: Optional[Any] = Field(default=None, alias="UnknownRelation", description="Unknown Relation")

class RelationshipInformation(_FlexModel):
    AdditionalCustomerName: Optional[str] = Field(default=None, alias="AdditionalCustomerName", description="Additional CustomerName to be updated")
    AdditionalLoginUserId: Optional[str] = Field(default=None, alias="AdditionalLoginUserId", description="Additional Login UserID to be updated")
    OtherReason: Optional[str] = Field(default=None, alias="OtherReason", description="Other Reason to be updated")
    RelationshipStatus: Optional[RelationshipStatus] = Field(default=None, alias="RelationshipStatus", description="RelationshipStatus to be updated")
    RelationshipType: Optional[CustomerRelationshipType] = Field(default=None, alias="RelationshipType", description="RelationshipType to be updated")
    RelationWithPrimaryLoginUser: Optional[ConnectionType] = Field(default=None, alias="RelationWithPrimaryLoginUser", description="Relation With Primary LoginUser to be updated")

class SingaporeData(_FlexModel):
    AnnualIncomeSgd: Optional[str] = Field(default=None, alias="AnnualIncomeSgd", description="Annual Income in Sgd")
    NetWorthSgd: Optional[str] = Field(default=None, alias="NetWorthSgd", description="Net Worth in Sgd")
    SgPermanentResident: Optional[bool] = Field(default=None, alias="SgPermanentResident", description="SG Permanent Resident")

class SwitzerlandData(_FlexModel):
    AnnualIncomeChf: Optional[str] = Field(default=None, alias="AnnualIncomeChf", description="Annual Income in Chf")
    NetWorthChf: Optional[str] = Field(default=None, alias="NetWorthChf", description="Net Worth in Chf")

class UkData(_FlexModel):
    EstimatedSavingAndInvestmentGbp: Optional[str] = Field(default=None, alias="EstimatedSavingAndInvestmentGbp", description="Estimated saving and investment in GBP")
    MonthlyIncomeAfterTaxGbp: Optional[str] = Field(default=None, alias="MonthlyIncomeAfterTaxGbp", description="Monthly income after tax in GBP")

class RenewalData(_FlexModel):
    AustraliaData: Optional[AustraliaData] = Field(default=None, alias="AustraliaData", description="Australia related data")
    FinlandData: Optional[FinlandData] = Field(default=None, alias="FinlandData", description="Finland related data")
    GlobalFinancialInformation: Optional[GlobalFinancialInformation] = Field(default=None, alias="GlobalFinancialInformation", description="Global finaincial information")
    HongkongData: Optional[HongkongData] = Field(default=None, alias="HongkongData", description="Hongkong related data")
    ItalyData: Optional[ItalyData] = Field(default=None, alias="ItalyData", description="Italy related data")
    JapanData: Optional[JapanData] = Field(default=None, alias="JapanData", description="Japan related data")
    PersonalInformation: Optional[PersonalInformation] = Field(default=None, alias="PersonalInformation", description="Personal Data")
    ProfileInformation: Optional[ProfileInformation] = Field(default=None, alias="ProfileInformation", description="Profile Data")
    RegulatoryInformation: Optional[RegulatoryInformation] = Field(default=None, alias="RegulatoryInformation", description="Regulatory Data")
    Relationships: Optional[List[RelationshipInformation]] = Field(default=None, alias="Relationships", description="Relationships data")
    SingaporeData: Optional[SingaporeData] = Field(default=None, alias="SingaporeData", description="Singapore related data")
    SwitzerlandData: Optional[SwitzerlandData] = Field(default=None, alias="SwitzerlandData", description="Switzerland related data")
    UkData: Optional[UkData] = Field(default=None, alias="UkData", description="UK related data")

class TypeOfTrigger(_FlexModel):
    ClientTriggered: Optional[Any] = Field(default=None, alias="ClientTriggered", description="For personal updates like address changes when no renewal exists already. If renewal already exists, same would be updated")
    TimeTrigger: Optional[Any] = Field(default=None, alias="TimeTrigger", description="Time Trigger ODD as per Saxo Compliance would be initiated on client if no renewal exists already. If renewal already exists, same would be updated wihout change in trigger")

class UpdateRenewalDataDocumentsforthegivenrenewalentityRequest(_FlexModel):
    Documents: Optional[List[RenewalDocument]] = Field(default=None, alias="Documents", description="Renewal documents to be uploaded")
    RenewalData: Optional[RenewalData] = Field(default=None, alias="RenewalData", description="Renewal data to be updated")
    RenewalEntityId: Optional[str] = Field(default=None, alias="RenewalEntityId", description="Renewal entity identifier")
    TypeOfTrigger: Optional[TypeOfTrigger] = Field(default=None, alias="TypeOfTrigger", description="Type Of Trigger to be selected")

class RenewalStatusContractType(_FlexModel):
    Corporate: Optional[Any] = Field(default=None, alias="Corporate", description="Corporate")
    JointAccount: Optional[Any] = Field(default=None, alias="JointAccount", description="JointAccount")
    LocalAssetSolution: Optional[Any] = Field(default=None, alias="LocalAssetSolution", description="LocalAssetSolution")
    Private: Optional[Any] = Field(default=None, alias="Private", description="Private")

class GetstatusofRenewalsRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    ContractId: Optional[str] = Field(default=None, alias="ContractId", description="Contract Id")
    ContractingEntity: Optional[List[str]] = Field(default=None, alias="ContractingEntity", description="List of Active Contracting Entity as present in CRM except for Swiss and Japan")
    ContractType: Optional[RenewalStatusContractType] = Field(default=None, alias="ContractType", description="Contract Type - Private, JointAccount, Corporate, LocalAssetSolution")
    SalesOffice: Optional[List[int]] = Field(default=None, alias="SalesOffice", description="List of Sales Office as present in CRM except for Swiss and Japan")
    UserInitial: Optional[str] = Field(default=None, alias="UserInitial", description="UserInitial")

class GetsrenewalstatusforclientsunderloggeduserorthepassedownerRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    MustRenewBy: Optional[str] = Field(default=None, alias="MustRenewBy", description="Optional, Date till which the pending renewals should be returned, default value is 30 days from today")
    OwnerKey: Optional[Any] = Field(default=None, alias="OwnerKey", description="Optional, ClientKey of the owner, whose subclient's renewal status is needed")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
