"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

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

class CorporateActionType(_FlexModel):
    Mandatory: Optional[Any] = Field(default=None, alias="Mandatory", description="Mandatory event: Event where no response is required and action is applied automatically.")
    Voluntary: Optional[Any] = Field(default=None, alias="Voluntary", description="Voluntary event: Event where a response is required. If no response is received before the reply deadline, the option marked as Default will be applied.")

class ElectionStatus(_FlexModel):
    Elected: Optional[Any] = Field(default=None, alias="Elected", description="Elected")
    NotElected: Optional[Any] = Field(default=None, alias="NotElected", description="Not elected")
    PartialElected: Optional[Any] = Field(default=None, alias="PartialElected", description="Partially elected")

class EventState(_FlexModel):
    Approved: Optional[Any] = Field(default=None, alias="Approved", description="Event in approved state")
    Cancelled: Optional[Any] = Field(default=None, alias="Cancelled", description="Event in cancelled state")
    Complete: Optional[Any] = Field(default=None, alias="Complete", description="Event in complete state")
    Confirmed: Optional[Any] = Field(default=None, alias="Confirmed", description="Event in confirmed state")
    Preliminary: Optional[Any] = Field(default=None, alias="Preliminary", description="Event in preliminary state")
    Withdrawn: Optional[Any] = Field(default=None, alias="Withdrawn", description="Event in withdrawn state")

class EventStatus(_FlexModel):
    Active: Optional[Any] = Field(default=None, alias="Active", description="Active events")
    Past: Optional[Any] = Field(default=None, alias="Past", description="Past events")
    Upcoming: Optional[Any] = Field(default=None, alias="Upcoming", description="Upcoming events")

class SortColumn(_FlexModel):
    AffectedAccounts: Optional[Any] = Field(default=None, alias="AffectedAccounts", description="Sort by number of accounts affected")
    AnnouncedDate: Optional[Any] = Field(default=None, alias="AnnouncedDate", description="Sort by announcement date")
    CorporateActionType: Optional[Any] = Field(default=None, alias="CorporateActionType", description="Sort by corporate action type")
    Date: Optional[Any] = Field(default=None, alias="Date", description="Sort by Date")
    EligibleHoldings: Optional[Any] = Field(default=None, alias="EligibleHoldings", description="Sort by total amount in holdings")
    EventId: Optional[Any] = Field(default=None, alias="EventId", description="Sort by event identifier")
    EventType: Optional[Any] = Field(default=None, alias="EventType", description="Sort by event type name")
    InstrumentDescription: Optional[Any] = Field(default=None, alias="InstrumentDescription", description="Sort by Instrument name/description")
    UpdatedDateTime: Optional[Any] = Field(default=None, alias="UpdatedDateTime", description="Sort by updated date time")

class SortType(_FlexModel):
    Asc: Optional[Any] = Field(default=None, alias="Asc", description="Ascending sort")
    Desc: Optional[Any] = Field(default=None, alias="Desc", description="Descending sort")

class GettheviewofcorporateactionsunderaparticularownerRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AssetTypes: Optional[List[AssetType]] = Field(default=None, alias="AssetTypes", description="Asset type filter for events.")
    CorporateActionTypes: Optional[List[CorporateActionType]] = Field(default=None, alias="CorporateActionTypes", description="Corporate action type filter for events.")
    ElectionStatuses: Optional[List[ElectionStatus]] = Field(default=None, alias="ElectionStatuses", description="Election status filter for events.")
    EventStates: Optional[List[EventState]] = Field(default=None, alias="EventStates", description="Filter collection based on event state. Note that some events are only returned if IncludeLapsedEvents is set to true.")
    EventStatus: Optional[EventStatus] = Field(default=None, alias="EventStatus", description="Event status filter.")
    EventTypes: Optional[List[str]] = Field(default=None, alias="EventTypes", description="Event type filter. Use event type codes to filter.")
    FromDeadlineDate: Optional[str] = Field(default=None, alias="FromDeadlineDate", description="Events on or after specified deadline date.")
    FromExDate: Optional[str] = Field(default=None, alias="FromExDate", description="Events on or after specified ex date.")
    FromPayDate: Optional[str] = Field(default=None, alias="FromPayDate", description="Events on or after specified pay date.")
    FromRecordDate: Optional[str] = Field(default=None, alias="FromRecordDate", description="Events on or after specified record date.")
    IncludeLapsedEvents: Optional[bool] = Field(default=None, alias="IncludeLapsedEvents", description="If true, the returned collection will include otherwise excluded events. These events have EventStatus of Past and an EventState of Preliminary, Cancelled, or Confirmed. These events are excluded by default due their low importance and excessive volumes.")
    Keywords: Optional[str] = Field(default=None, alias="Keywords", description="Looks for keywords in instrument description, ISIN code, and instrument symbol.")
    OwnerKey: Optional[Any] = Field(default=None, alias="OwnerKey", description="Unique key identifying the owner. This is the clientKey of the owner under which corporate actions will be queried. Default: Logged-in user's client.")
    SortColumn: Optional[SortColumn] = Field(default=None, alias="SortColumn", description="Specify a column to sort on. Default sort will be provided on Date.")
    SortType: Optional[SortType] = Field(default=None, alias="SortType", description="Specify ascending or descending sort. Default sort type will be Descending.")
    ToDeadlineDate: Optional[str] = Field(default=None, alias="ToDeadlineDate", description="Events on or before specified deadline date.")
    ToExDate: Optional[str] = Field(default=None, alias="ToExDate", description="Events on or before specified ex date.")
    ToPayDate: Optional[str] = Field(default=None, alias="ToPayDate", description="Events on or before specified pay date.")
    ToRecordDate: Optional[str] = Field(default=None, alias="ToRecordDate", description="Events on or before specified record date.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
