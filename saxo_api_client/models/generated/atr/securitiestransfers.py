"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetlistofbrokersforthegivenISOCountryCodeRequest(_FlexModel):
    CountryCode: Optional[Any] = Field(default=None, alias="CountryCode", description="ISO Country Code")

class GetdetailsofanInterAccountSecurityTransferRequestRequest(_FlexModel):
    UniqueReference: Optional[str] = Field(default=None, alias="UniqueReference", description="Unique Reference")

class TransferableAssetType(_FlexModel):
    Bond: Optional[Any] = Field(default=None, alias="Bond", description="Bond")
    CertificateBonus: Optional[Any] = Field(default=None, alias="CertificateBonus", description="CertificateBonus")
    CertificateCappedBonus: Optional[Any] = Field(default=None, alias="CertificateCappedBonus", description="CertificateCappedBonus")
    CertificateCappedCapitalProtected: Optional[Any] = Field(default=None, alias="CertificateCappedCapitalProtected", description="CertificateCappedCapitalProtected")
    CertificateCappedOutperformance: Optional[Any] = Field(default=None, alias="CertificateCappedOutperformance", description="CertificateCappedOutperformance")
    CertificateConstantLeverage: Optional[Any] = Field(default=None, alias="CertificateConstantLeverage", description="CertificateConstantLeverage")
    CertificateDiscount: Optional[Any] = Field(default=None, alias="CertificateDiscount", description="CertificateDiscount")
    CertificateExpress: Optional[Any] = Field(default=None, alias="CertificateExpress", description="CertificateExpress")
    CertificateTracker: Optional[Any] = Field(default=None, alias="CertificateTracker", description="CertificateTracker")
    CertificateUncappedCapitalProtection: Optional[Any] = Field(default=None, alias="CertificateUncappedCapitalProtection", description="CertificateUncappedCapitalProtection")
    CertificateUncappedOutperformance: Optional[Any] = Field(default=None, alias="CertificateUncappedOutperformance", description="CertificateUncappedOutperformance")
    CompanyWarrant: Optional[Any] = Field(default=None, alias="CompanyWarrant", description="Unlisted warrant issued by a corporation, often physically settled.")
    Etc: Optional[Any] = Field(default=None, alias="Etc", description="Etc")
    Etf: Optional[Any] = Field(default=None, alias="Etf", description="Exchange traded fund.")
    Etn: Optional[Any] = Field(default=None, alias="Etn", description="Etn")
    Fund: Optional[Any] = Field(default=None, alias="Fund", description="Fund")
    MiniFuture: Optional[Any] = Field(default=None, alias="MiniFuture", description="MiniFuture")
    MutualFund: Optional[Any] = Field(default=None, alias="MutualFund", description="Mututal Funds")
    Rights: Optional[Any] = Field(default=None, alias="Rights", description="Rights")
    Stock: Optional[Any] = Field(default=None, alias="Stock", description="Stock")
    Warrant: Optional[Any] = Field(default=None, alias="Warrant", description="Warrant")
    WarrantDoubleKnockOut: Optional[Any] = Field(default=None, alias="WarrantDoubleKnockOut", description="")
    WarrantKnockOut: Optional[Any] = Field(default=None, alias="WarrantKnockOut", description="WarrantKnockOut")
    WarrantOpenEndKnockOut: Optional[Any] = Field(default=None, alias="WarrantOpenEndKnockOut", description="WarrantOpenEndKnockOut")
    WarrantSpread: Optional[Any] = Field(default=None, alias="WarrantSpread", description="")

class BeneficialOwnershipChange(_FlexModel):
    CBO: Optional[Any] = Field(default=None, alias="CBO", description="Change in Beneficial Ownership.")
    NCBO: Optional[Any] = Field(default=None, alias="NCBO", description="No Change in Beneficial Ownership")

class TransferType(_FlexModel):
    New: Optional[Any] = Field(default=None, alias="New", description="New Transfer Request")
    Reversal: Optional[Any] = Field(default=None, alias="Reversal", description="Reversal of an existing transfer request.")

class SubmitInterAccountSecurityTransferRequestRequest(_FlexModel):
    AssetType: Optional[TransferableAssetType] = Field(default=None, alias="AssetType", description="AssetType of the security")
    BeneficialOwnershipChange: Optional[BeneficialOwnershipChange] = Field(default=None, alias="BeneficialOwnershipChange", description="Change in Beneficial Ownership.")
    FromAccountKey: Optional[Any] = Field(default=None, alias="FromAccountKey", description="The from account identifier in key format from which securities transfer is executed")
    Price: Optional[float] = Field(default=None, alias="Price", description="The price per security")
    Quantity: Optional[float] = Field(default=None, alias="Quantity", description="Quantity of security to transfer")
    ReversalReference: Optional[str] = Field(default=None, alias="ReversalReference", description="Oriningal reference Reference Number for the reversal request.")
    ToAccountKey: Optional[Any] = Field(default=None, alias="ToAccountKey", description="The to account identifier in key format to which securities transfer is executed")
    TransferType: Optional[TransferType] = Field(default=None, alias="TransferType", description="Position Transfer Action New/Reversal.")
    Uic: Optional[int] = Field(default=None, alias="Uic", description="Uic of the security")
    UniqueReference: Optional[str] = Field(default=None, alias="UniqueReference", description="Unique reference Reference Number for the request.")

class GetlistofSecurityTransfersexecutedbyclientbasedonlistofcommaseparatedtransferidsRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The client identifier in key format")
    TransferIds: Optional[List[str]] = Field(default=None, alias="TransferIds", description="Comma separate list of Transfer IDs")

class Broker(_FlexModel):
    BrokerType: Optional[str] = Field(default=None, alias="BrokerType", description="BrokerType")
    Contact: Optional[str] = Field(default=None, alias="Contact", description="Broker Contact")
    CountryCode: Optional[Any] = Field(default=None, alias="CountryCode", description="Broker's Country Id")
    Email: Optional[str] = Field(default=None, alias="Email", description="Broker Email")
    Id: Optional[int] = Field(default=None, alias="Id", description="Id")
    Name: Optional[str] = Field(default=None, alias="Name", description="Broker Name")
    Phone: Optional[str] = Field(default=None, alias="Phone", description="Broker Phone Number")

class ReasonCode(_FlexModel):
    SecurityTransferReasonCodeOutAdministrationTooChallenging: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutAdministrationTooChallenging", description="")
    SecurityTransferReasonCodeOutConsolidatingInvestmentsWithAnotherProvider: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutConsolidatingInvestmentsWithAnotherProvider", description="")
    SecurityTransferReasonCodeOutDoNotEnjoyUsingSaxoPlatformOrApp: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutDoNotEnjoyUsingSaxoPlatformOrApp", description="")
    SecurityTransferReasonCodeOutEducationalContentDoesNotMeetNeeds: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutEducationalContentDoesNotMeetNeeds", description="")
    SecurityTransferReasonCodeOutInteractionsWithSaxoNotMetExpectations: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutInteractionsWithSaxoNotMetExpectations", description="")
    SecurityTransferReasonCodeOutMovingToAnotherCountry: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutMovingToAnotherCountry", description="")
    SecurityTransferReasonCodeOutNotSpecified: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutNotSpecified", description="")
    SecurityTransferReasonCodeOutOther: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutOther", description="")
    SecurityTransferReasonCodeOutPositionDelistedOrNotSupportedAtSaxo: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutPositionDelistedOrNotSupportedAtSaxo", description="")
    SecurityTransferReasonCodeOutPreferNotToSay: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutPreferNotToSay", description="")
    SecurityTransferReasonCodeOutRegulatoryReasons: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutRegulatoryReasons", description="")
    SecurityTransferReasonCodeOutSatisfiedWithPricingFeesAtAnotherProvider: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutSatisfiedWithPricingFeesAtAnotherProvider", description="")
    SecurityTransferReasonCodeOutSaxoCommunications: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutSaxoCommunications", description="")
    SecurityTransferReasonCodeOutUnableToTradeProductsIWant: Optional[Any] = Field(default=None, alias="SecurityTransferReasonCodeOutUnableToTradeProductsIWant", description="")

class SecurityTransferReason(_FlexModel):
    OtherText: Optional[str] = Field(default=None, alias="OtherText", description="user comment in case reason code is other.")
    ReasonCode: Optional[ReasonCode] = Field(default=None, alias="ReasonCode", description="Reason code for security transfer.")

class Security(_FlexModel):
    Currency: Optional[str] = Field(default=None, alias="Currency", description="The Currency of the security to be transferred.")
    Description: Optional[str] = Field(default=None, alias="Description", description="The Description of the security")
    Exchange: Optional[str] = Field(default=None, alias="Exchange", description="The Exchange where the security gets transferred.")
    ExchangeText: Optional[str] = Field(default=None, alias="ExchangeText", description="ExchangeText of the security.")
    InstrumentSymbolCode: Optional[str] = Field(default=None, alias="InstrumentSymbolCode", description="The InstrumentSymbolCode of the security.")
    IsinCode: Optional[str] = Field(default=None, alias="IsinCode", description="IsinCode of the security.")
    Price: Optional[float] = Field(default=None, alias="Price", description="The price per security")
    PurchaseDate: Optional[str] = Field(default=None, alias="PurchaseDate", description="Purchase date of instrument")
    Quantity: Optional[float] = Field(default=None, alias="Quantity", description="Quantity of security to transfer")
    SpecialInstructions: Optional[List[int]] = Field(default=None, alias="SpecialInstructions", description="The Instruction set for the transfer request.")
    Uic: Optional[int] = Field(default=None, alias="Uic", description="Uic of the security")

class BuyerSellerCodeType(_FlexModel):
    Bic: Optional[Any] = Field(default=None, alias="Bic", description="Bic")
    Cdident: Optional[Any] = Field(default=None, alias="Cdident", description="Cdident")
    Local: Optional[Any] = Field(default=None, alias="Local", description="Local")
    None_: Optional[Any] = Field(default=None, alias="None", description="None")
    Text: Optional[Any] = Field(default=None, alias="Text", description="Text")

class ClearingAgentCodeType(_FlexModel):
    Bic: Optional[Any] = Field(default=None, alias="Bic", description="Bic")
    Local: Optional[Any] = Field(default=None, alias="Local", description="Local")
    None_: Optional[Any] = Field(default=None, alias="None", description="None")

class SettlementInstruction(_FlexModel):
    AccountAtClearingAgent: Optional[str] = Field(default=None, alias="AccountAtClearingAgent", description="The safekeeping / Security account at the custody of the client")
    AgentLocalAccount: Optional[str] = Field(default=None, alias="AgentLocalAccount", description="The agent local account")
    BuyerSellerCode: Optional[str] = Field(default=None, alias="BuyerSellerCode", description="The buyer seller code")
    BuyerSellerCodeType: Optional[BuyerSellerCodeType] = Field(default=None, alias="BuyerSellerCodeType", description="The BIC Code / Local Code of the custody of the client with their counterpart")
    ClearingAgentCode: Optional[str] = Field(default=None, alias="ClearingAgentCode", description="The clearing agent code")
    ClearingAgentCodeType: Optional[ClearingAgentCodeType] = Field(default=None, alias="ClearingAgentCodeType", description="The BIC / Local Code of the Exchange of the instrument. For example if client is trading in UK Share then the Clearing Agent would be the BIC / Local Code from UK")
    FreeText: Optional[str] = Field(default=None, alias="FreeText", description="The information / remarks")
    SettlementAgentAccount: Optional[str] = Field(default=None, alias="SettlementAgentAccount", description="The settlement agent account")

class TransferDirection(_FlexModel):
    TransferIn: Optional[Any] = Field(default=None, alias="TransferIn", description="Transfer securities from external broker to Saxo Bank")
    TransferOut: Optional[Any] = Field(default=None, alias="TransferOut", description="Transfer securities Saxo Bank to external broker")

class SubmitSecuritiesTransferRequestRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account identifier in key format from which securities transfer is executed")
    AssetType: Optional[TransferableAssetType] = Field(default=None, alias="AssetType", description="The asset type to be transferred")
    Broker: Optional[Broker] = Field(default=None, alias="Broker", description="The client's broker details")
    ClientAccountAtBroker: Optional[str] = Field(default=None, alias="ClientAccountAtBroker", description="Identifier of the client's account at the broker")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The client identifier in key format for which system will execute securities transfer")
    Reason: Optional[SecurityTransferReason] = Field(default=None, alias="Reason", description="default constructor")
    Securities: Optional[List[Security]] = Field(default=None, alias="Securities", description="The securities details")
    SettlementDate: Optional[str] = Field(default=None, alias="SettlementDate", description="The settlement date")
    SettlementInstruction: Optional[SettlementInstruction] = Field(default=None, alias="SettlementInstruction", description="Settlement Instruction")
    TradeDate: Optional[str] = Field(default=None, alias="TradeDate", description="The agreed trade date")
    TransferDirection: Optional[TransferDirection] = Field(default=None, alias="TransferDirection", description="Transfer type, in or out of Bank")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
