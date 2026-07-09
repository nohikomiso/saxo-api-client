"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetstandinginstructionsRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Client Key to fetch standing instructions for.")
    IncludeSubAccounts: Optional[bool] = Field(default=None, alias="IncludeSubAccounts", description="Indicates whether to include standing instructions from sub-clients.")

class AssetType(_FlexModel):
    Bond: Optional[Any] = Field(default=None, alias="Bond", description="Bond.")
    CertificateBonus: Optional[Any] = Field(default=None, alias="CertificateBonus", description="Mirrors the price movement of the underlying only if and when the underlying price exceeds the defined barrier. If the certificate expires below the barrier, it offers partial protection/return of investment.")
    CertificateCappedBonus: Optional[Any] = Field(default=None, alias="CertificateCappedBonus", description="Certificate Capped Bonus.")
    CertificateCappedCapitalProtected: Optional[Any] = Field(default=None, alias="CertificateCappedCapitalProtected", description="Guarantees a capped percentage increase of the underlying asset's value above the issue price at expiry/maturity. Max loss is the amount invested multiplied by the CapitalProtection percentage.")
    CertificateCappedOutperformance: Optional[Any] = Field(default=None, alias="CertificateCappedOutperformance", description="Capped Outperformance Certificate.")
    CertificateConstantLeverage: Optional[Any] = Field(default=None, alias="CertificateConstantLeverage", description="Certificate Constant Leverage.")
    CertificateDiscount: Optional[Any] = Field(default=None, alias="CertificateDiscount", description="Yields a capped return if the underlying asset's value is above the specified cap level at expiry. If the underlying's value is below the strike at expiry, the investor received the underlying or equivalent value. Offers direct exposure in underlying at a lower price (discount) with a capped potential profit and limited loss.")
    CertificateExpress: Optional[Any] = Field(default=None, alias="CertificateExpress", description="Certificate Express kick out.")
    CertificateTracker: Optional[Any] = Field(default=None, alias="CertificateTracker", description="A certificate that mirrors the price movement of the underlying instrument. Often used to trade movements in indicies. Movements can be a fixed ratio of the underlying and can be inverted for bearish/short speculation. Risk is equivalent to owning the underlying.")
    CertificateUncappedCapitalProtection: Optional[Any] = Field(default=None, alias="CertificateUncappedCapitalProtection", description="Guarantees a percentage increase of the underlying asset's value above the issue price at expiry/maturity. Max loss is the amount invested multiplied by the CapitalProtection percentage.")
    CertificateUncappedOutperformance: Optional[Any] = Field(default=None, alias="CertificateUncappedOutperformance", description="Provides leveraged returns when the underlying price exceeds the threshold strike price. The amount leverage is defined by the Participation %. When the underlying is below the strike price, the certificate mirrors the underlying price 1:1.")
    CfdOnCompanyWarrant: Optional[Any] = Field(default=None, alias="CfdOnCompanyWarrant", description="Cfd on unlisted warrant issued by a corporation.")
    CfdOnEtc: Optional[Any] = Field(default=None, alias="CfdOnEtc", description="Cfd on Etc")
    CfdOnEtf: Optional[Any] = Field(default=None, alias="CfdOnEtf", description="Cfd on Etf")
    CfdOnEtn: Optional[Any] = Field(default=None, alias="CfdOnEtn", description="Cfd on Etn")
    CfdOnFund: Optional[Any] = Field(default=None, alias="CfdOnFund", description="Cfd on Fund")
    CfdOnRights: Optional[Any] = Field(default=None, alias="CfdOnRights", description="Cfd on Rights")
    CfdOnStock: Optional[Any] = Field(default=None, alias="CfdOnStock", description="Cfd on Stock.")
    CompanyWarrant: Optional[Any] = Field(default=None, alias="CompanyWarrant", description="Unlisted warrant issued by a corporation, often physically settled.")
    MiniFuture: Optional[Any] = Field(default=None, alias="MiniFuture", description="MiniFuture.")
    MutualFund: Optional[Any] = Field(default=None, alias="MutualFund", description="Mutual Fund.")
    Stock: Optional[Any] = Field(default=None, alias="Stock", description="Stock.")
    Warrant: Optional[Any] = Field(default=None, alias="Warrant", description="Warrant")
    WarrantDoubleKnockOut: Optional[Any] = Field(default=None, alias="WarrantDoubleKnockOut", description="Warrant with two knock-out barriers.")
    WarrantKnockOut: Optional[Any] = Field(default=None, alias="WarrantKnockOut", description="Warrant with a knock-out barrier.")
    WarrantOpenEndKnockOut: Optional[Any] = Field(default=None, alias="WarrantOpenEndKnockOut", description="Knock-out Warrant with no expiry.")
    WarrantSpread: Optional[Any] = Field(default=None, alias="WarrantSpread", description="Warrant with built-in spread.")

class OptionType(_FlexModel):
    CASH: Optional[Any] = Field(default=None, alias="CASH", description="Cash")
    SECU: Optional[Any] = Field(default=None, alias="SECU", description="Security")

class Instruction(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Account Identifier")
    AssetType: Optional[AssetType] = Field(default=None, alias="AssetType", description="Asset Type")
    OptionType: Optional[OptionType] = Field(default=None, alias="OptionType", description="The type of option to automatically elect. Must be either SECU or CASH.")
    Uic: Optional[int] = Field(default=None, alias="Uic", description="The instrument that this standing instruction applies to.")

class CreatenewstandinginstructionRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Client identifier")
    StandingInstructions: Optional[List[Instruction]] = Field(default=None, alias="StandingInstructions", description="Standing Instructions")

class DeletestandinginstructionsRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Client Identifier Key")
    StandingInstructionIds: Optional[List[str]] = Field(default=None, alias="StandingInstructionIds", description="Standing instruction ids to delete.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
