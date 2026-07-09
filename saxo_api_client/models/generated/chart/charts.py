"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class AssetType(_FlexModel):
    Bond: Optional[Any] = Field(default=None, alias="Bond", description="Bond.")
    Cash: Optional[Any] = Field(default=None, alias="Cash", description="Cash. Not tradeable!")
    CBBCCategoryN: Optional[Any] = Field(default=None, alias="CBBCCategoryN", description="Callable Bull/Bear Contract Category N. Call price or level is equal to its strike price or level, under which you will not receive any cash payment after the occurrence of a mandatory call event, and will lose your entire investment.")
    CBBCCategoryR: Optional[Any] = Field(default=None, alias="CBBCCategoryR", description="Callable Bull/Bear Contract Category R. Call price or level is different from its strike price or level, and you may receive a residual cash payment (called 'residual value') upon the occurrence of a mandatory call event. However, in the worst case, you will not receive any residual value and will lose your entire investment.")
    CertificateBarrierDiscount: Optional[Any] = Field(default=None, alias="CertificateBarrierDiscount", description="A Discount Certificate with Barrier allows investors with moderate to high risk tolerance to buy a selected underlying asset at a discount. The more favorable entry price gives a yield advantage, so that an attractive return is possible even in a sideways market.")
    CertificateBarrierReverseConvertibles: Optional[Any] = Field(default=None, alias="CertificateBarrierReverseConvertibles", description="With Barrier Reverse Convertibles investors with a moderate-to-high risk tolerance in sideways moving markets can optimize their opportunities to earn yields thanks to a coupon. As in the Reverse Convertibles, the coupon is always paid out. The type and amount of the repayment of the nominal amount on expiry is aligned to the price of the underlying asset (e.g. individual equity, share index, equity basket, currency pair or commodity).")
    CertificateBonus: Optional[Any] = Field(default=None, alias="CertificateBonus", description="Mirrors the price movement of the underlying only if and when the underlying price exceeds the defined barrier. If the certificate expires below the barrier, it offers partial protection/return of investment.")
    CertificateCapitalProtectionWithCoupon: Optional[Any] = Field(default=None, alias="CertificateCapitalProtectionWithCoupon", description="Capital protection certificates with coupon, also known as Coupon CPNs, are capital protected at maturity. This means that at the end of the usually multi-year term, you will always receive at least 90% of the nominal amount back. Depending on the features, the capital protection is usually between 90% and 100% of the nominal value.")
    CertificateCapitalProtectionWithKnockOut: Optional[Any] = Field(default=None, alias="CertificateCapitalProtectionWithKnockOut", description="Capital Protection Certificates with Barrier, also known as Barrier CPNs or Dolphin CPNs, are capital protected at maturity. The capital protection usually amounts to 90 - 100 percent of the nominal value, so that at maturity you will be paid back at least 90% of the capital invested at issue - regardless of the underlying asset.")
    CertificateCappedBonus: Optional[Any] = Field(default=None, alias="CertificateCappedBonus", description="Certificate Capped Bonus.")
    CertificateCappedCapitalProtected: Optional[Any] = Field(default=None, alias="CertificateCappedCapitalProtected", description="Guarantees a capped percentage increase of the underlying asset's value above the issue price at expiry/maturity. Max loss is the amount invested multiplied by the CapitalProtection percentage.")
    CertificateCappedOutperformance: Optional[Any] = Field(default=None, alias="CertificateCappedOutperformance", description="Capped Outperformance Certificate.")
    CertificateConstantLeverage: Optional[Any] = Field(default=None, alias="CertificateConstantLeverage", description="Certificate Constant Leverage.")
    CertificateDiscount: Optional[Any] = Field(default=None, alias="CertificateDiscount", description="Yields a capped return if the underlying asset's value is above the specified cap level at expiry. If the underlying's value is below the strike at expiry, the investor received the underlying or equivalent value. Offers direct exposure in underlying at a lower price (discount) with a capped potential profit and limited loss.")
    CertificateExpress: Optional[Any] = Field(default=None, alias="CertificateExpress", description="Certificate Express kick out.")
    CertificateOtherCapitalProtection: Optional[Any] = Field(default=None, alias="CertificateOtherCapitalProtection", description="Capital protection products are the most defensive form of Investment Products and are therefore suitable for investors with a low to moderate risk tolerance.")
    CertificateOtherConstantLeverage: Optional[Any] = Field(default=None, alias="CertificateOtherConstantLeverage", description="Constant Leverage Certificates, aka Factor Certificates, enable investors who are willing to take risks to participate disproportionately in the price performance of an underlying asset (e.g. equities, indices, commodities or currency pairs)")
    CertificateOtherParticipation: Optional[Any] = Field(default=None, alias="CertificateOtherParticipation", description="Participation products are covered by Tracker Certificates. These Certificates are suitable for investors with a medium to high risk preference who want to participate cost efficiently and unlimitedly in the price development of a single stock, a market or a market segment.")
    CertificateOtherYieldEnhancement: Optional[Any] = Field(default=None, alias="CertificateOtherYieldEnhancement", description="Investment Products aimed at optimizing yields offer partial protection. This can provide attractive returns even when the price of the respective underlying asset just remains stationary up to maturity.")
    CertificateOutperformanceBonus: Optional[Any] = Field(default=None, alias="CertificateOutperformanceBonus", description="With Bonus-Outperformance Certificates, you can apply leverage, since Bonus-Outperformance Certificates offer you the chance to participate disproportionately and without restriction in rising prices of the underlying asset (e.g. an equity, an index or a currency pair). This means that as of a predefined price level (the so-called strike level) participation in a potentially rising price performance is higher than 100%. The exact performance rate varies depending on the product features and is fixed per issue.")
    CertificateReverseConvertibles: Optional[Any] = Field(default=None, alias="CertificateReverseConvertibles", description="With Reverse Convertibles investors with a moderate-to-high risk tolerance in sideways moving markets can optimize their opportunities to earn yields thanks to a coupon. While the coupon is always paid out, the type and amount of the repayment of the nominal amount on expiration is aligned to the price of the underlying asset (e.g. individual equity, share index, equity basket, currency pair or commodity).")
    CertificateTracker: Optional[Any] = Field(default=None, alias="CertificateTracker", description="A certificate that mirrors the price movement of the underlying instrument. Often used to trade movements in indicies. Movements can be a fixed ratio of the underlying and can be inverted for bearish/short speculation. Risk is equivalent to owning the underlying.")
    CertificateTwinWin: Optional[Any] = Field(default=None, alias="CertificateTwinWin", description="With Twin-Win Certificates, you can pull off a remarkable balancing act on the markets, i.e. whether the underlying asset (e.g. equity or index) rises or falls, you can profit in both cases. In doing so, you participate 1:1 in price gains of the underlying asset over and above the strike price without restriction (taking into account the subscription ratio). Price losses below the strike price are, on the other hand, converted accordingly on the due date if the price of the underlying asset has never fallen to or below a specific barrier (Knock-Out Level) during the term. However, after a barrier has been broken the conversion of prices losses of the underlying asset into gains ceases to apply. Instead, in this case Twin-Win Certificates behave like conventional Tracker Certificates, so that price losses of the underlying asset (under the strike price) lead to corresponding losses in the certificate.")
    CertificateUncappedCapitalProtection: Optional[Any] = Field(default=None, alias="CertificateUncappedCapitalProtection", description="Guarantees a percentage increase of the underlying asset's value above the issue price at expiry/maturity. Max loss is the amount invested multiplied by the CapitalProtection percentage.")
    CertificateUncappedOutperformance: Optional[Any] = Field(default=None, alias="CertificateUncappedOutperformance", description="Provides leveraged returns when the underlying price exceeds the threshold strike price. The amount leverage is defined by the Participation %. When the underlying is below the strike price, the certificate mirrors the underlying price 1:1.")
    CfdIndexOption: Optional[Any] = Field(default=None, alias="CfdIndexOption", description="Cfd Index Option.")
    CfdOnCompanyWarrant: Optional[Any] = Field(default=None, alias="CfdOnCompanyWarrant", description="Cfd on unlisted warrant issued by a corporation.")
    CfdOnEtc: Optional[Any] = Field(default=None, alias="CfdOnEtc", description="Cfd on Etc")
    CfdOnEtf: Optional[Any] = Field(default=None, alias="CfdOnEtf", description="Cfd on Etf")
    CfdOnEtn: Optional[Any] = Field(default=None, alias="CfdOnEtn", description="Cfd on Etn")
    CfdOnFund: Optional[Any] = Field(default=None, alias="CfdOnFund", description="Cfd on Fund")
    CfdOnFutures: Optional[Any] = Field(default=None, alias="CfdOnFutures", description="Cfd on Futures.")
    CfdOnIndex: Optional[Any] = Field(default=None, alias="CfdOnIndex", description="Cfd on Stock Index.")
    CfdOnRights: Optional[Any] = Field(default=None, alias="CfdOnRights", description="Cfd on Rights")
    CfdOnStock: Optional[Any] = Field(default=None, alias="CfdOnStock", description="Cfd on Stock.")
    CompanyWarrant: Optional[Any] = Field(default=None, alias="CompanyWarrant", description="Unlisted warrant issued by a corporation, often physically settled.")
    ContractFutures: Optional[Any] = Field(default=None, alias="ContractFutures", description="Contract Futures.")
    Etc: Optional[Any] = Field(default=None, alias="Etc", description="Etc")
    Etf: Optional[Any] = Field(default=None, alias="Etf", description="Exchange traded fund.")
    Etn: Optional[Any] = Field(default=None, alias="Etn", description="Etn")
    Fund: Optional[Any] = Field(default=None, alias="Fund", description="Fund")
    FuturesOption: Optional[Any] = Field(default=None, alias="FuturesOption", description="Futures Option.")
    FuturesStrategy: Optional[Any] = Field(default=None, alias="FuturesStrategy", description="Futures Strategy.")
    FxBinaryOption: Optional[Any] = Field(default=None, alias="FxBinaryOption", description="Forex Binary Option.")
    FxCrypto: Optional[Any] = Field(default=None, alias="FxCrypto", description="Forex Crypto Currency.")
    FxForwards: Optional[Any] = Field(default=None, alias="FxForwards", description="Forex Forward.")
    FxKnockInOption: Optional[Any] = Field(default=None, alias="FxKnockInOption", description="Forex Knock In Option.")
    FxKnockOutOption: Optional[Any] = Field(default=None, alias="FxKnockOutOption", description="Forex Knock Out Option.")
    FxNoTouchOption: Optional[Any] = Field(default=None, alias="FxNoTouchOption", description="Forex No Touch Option.")
    FxOneTouchOption: Optional[Any] = Field(default=None, alias="FxOneTouchOption", description="Forex One Touch Option.")
    FxSpot: Optional[Any] = Field(default=None, alias="FxSpot", description="Forex Spot.")
    FxSwap: Optional[Any] = Field(default=None, alias="FxSwap", description="Forex Swap.")
    FxVanillaOption: Optional[Any] = Field(default=None, alias="FxVanillaOption", description="Forex Vanilla Option.")
    GuaranteeNote: Optional[Any] = Field(default=None, alias="GuaranteeNote", description="Danish investment scheme (“Grantbevis”). Not online tradeable.")
    InlineWarrant: Optional[Any] = Field(default=None, alias="InlineWarrant", description="Inline Warrants. Holders receive a pre-determined amount that depends on whether an underlying asset falls at, or within or outside the upper and lower strikes at expiry.")
    IpoOnStock: Optional[Any] = Field(default=None, alias="IpoOnStock", description="IPO on Stock")
    ManagedFund_Obsolete: Optional[Any] = Field(default=None, alias="ManagedFund Obsolete", description=": Managed Fund.")
    MiniFuture: Optional[Any] = Field(default=None, alias="MiniFuture", description="MiniFuture.")
    MutualFund: Optional[Any] = Field(default=None, alias="MutualFund", description="Mutual Fund.")
    PortfolioNote: Optional[Any] = Field(default=None, alias="PortfolioNote", description="Danish pooled investment scheme (“Pulje”). Not online tradeable.")
    Rights: Optional[Any] = Field(default=None, alias="Rights", description="Rights")
    SrdOnEtf: Optional[Any] = Field(default=None, alias="SrdOnEtf", description="SRD. (Service de Règlement Différé) on Etf.")
    SrdOnStock: Optional[Any] = Field(default=None, alias="SrdOnStock", description="SRD. (Service de Règlement Différé) on Stock.")
    Stock: Optional[Any] = Field(default=None, alias="Stock", description="Stock.")
    StockIndex: Optional[Any] = Field(default=None, alias="StockIndex", description="Stock Index.")
    StockIndexOption: Optional[Any] = Field(default=None, alias="StockIndexOption", description="Stock Index Option.")
    StockOption: Optional[Any] = Field(default=None, alias="StockOption", description="Stock Option.")
    SubscriptionOnCertificate: Optional[Any] = Field(default=None, alias="SubscriptionOnCertificate", description="Used for IPO/Subscription.")
    Warrant: Optional[Any] = Field(default=None, alias="Warrant", description="Warrant")
    WarrantDoubleKnockOut: Optional[Any] = Field(default=None, alias="WarrantDoubleKnockOut", description="Warrant with two knock-out barriers.")
    WarrantKnockOut: Optional[Any] = Field(default=None, alias="WarrantKnockOut", description="Warrant with a knock-out barrier.")
    WarrantOpenEndKnockOut: Optional[Any] = Field(default=None, alias="WarrantOpenEndKnockOut", description="Knock-out Warrant with no expiry.")
    WarrantOtherLeverageWithKnockOut: Optional[Any] = Field(default=None, alias="WarrantOtherLeverageWithKnockOut", description="In the case of Warrants with Knock-Out, aka Turbos, the name says it all. With these investment instruments, investors who are willing to take risks can shift into turbo and considerably increase their yield potential.")
    WarrantOtherLeverageWithoutKnockOut: Optional[Any] = Field(default=None, alias="WarrantOtherLeverageWithoutKnockOut", description="Warrants allow investors who are willing to take risks can choose between Call and Put Warrants. Call Warrants benefit from rising prices of the underlying asset whereas. Put Warrants rely on falling prices of the underlying asset.")
    WarrantSpread: Optional[Any] = Field(default=None, alias="WarrantSpread", description="Warrant with built-in spread.")

class ChartSampleFieldSet(_FlexModel):
    BidAsk: Optional[Any] = Field(default=None, alias="BidAsk", description="Return the OpenBid/Ask, HighBid/Ask, LowBid/Ask and CloseBid/Ask values.")
    Default: Optional[Any] = Field(default=None, alias="Default", description="Return the default set of fields for the specified asset type, please see the learn section for details.")
    LastTraded: Optional[Any] = Field(default=None, alias="LastTraded", description="Return the Open, High, Low, Close values along with Interest and Volume.")

class ChartFieldGroupSpec(_FlexModel):
    ChartInfo: Optional[Any] = Field(default=None, alias="ChartInfo", description="Add field group ChartInfo to get additional information about the OHLC samples.")
    Data: Optional[Any] = Field(default=None, alias="Data", description="Add FieldGroup Data to include the OHLC samples. If omitted while other field groups are included then the samples are not included in the response.")
    DisplayAndFormat: Optional[Any] = Field(default=None, alias="DisplayAndFormat", description="Add FieldGroup DisplayAndFormat to include formatting and display information about the instrument.")

class ChartRequestMode(_FlexModel):
    From: Optional[Any] = Field(default=None, alias="From", description="From")
    UpTo: Optional[Any] = Field(default=None, alias="UpTo", description="Up to")

class GetchartdataRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Optional")
    AssetType: Optional[AssetType] = Field(default=None, alias="AssetType", description="Asset type of the instrument.")
    ChartSampleFieldSet: Optional[ChartSampleFieldSet] = Field(default=None, alias="ChartSampleFieldSet", description="Optionally select which set of fields are returned in the Data array. Currently only applicable for asset types (Warrants, MiniFutures and Certificates).")
    Count: Optional[int] = Field(default=None, alias="Count", description="Optionally specifies maximum number of samples to return, max 1200, default 1200.")
    FieldGroups: Optional[List[ChartFieldGroupSpec]] = Field(default=None, alias="FieldGroups", description="Specifies which data to return. Default is [Data]")
    Horizon: Optional[int] = Field(default=None, alias="Horizon", description="The time period that each sample covers. Values are interpreted in minutes: 1, 2, 3, 5, 10, 15, 30, 60, 120, 180, 240, 300, 360, 480, 1440, 10080, 43200, 129600, 518400.")
    Mode: Optional[ChartRequestMode] = Field(default=None, alias="Mode", description="If Time is supplied, mode specifies if the endpoint should returns samples 'UpTo' (and including) or 'From' (and including) the specified time.")
    Time: Optional[str] = Field(default=None, alias="Time", description="Specifies the time of a sample, which must either be the first (If Mode=='From') or the last (if Mode=='UpTo') in the returned data.")
    Uic: Optional[int] = Field(default=None, alias="Uic", description="Uic of the instrument.")

class DataSeriesType(_FlexModel):
    Growth: Optional[Any] = Field(default=None, alias="Growth", description="")
    Price: Optional[Any] = Field(default=None, alias="Price", description="")

class ChartSubscriptionRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Optional")
    AssetType: Optional[AssetType] = Field(default=None, alias="AssetType", description="Asset type of the instrument.")
    ChartSampleFieldSet: Optional[ChartSampleFieldSet] = Field(default=None, alias="ChartSampleFieldSet", description="Optionally select which set of fields are returned in the Data array. Currently only applicable for asset types (Warrants, MiniFutures and Certificates).")
    Count: Optional[int] = Field(default=None, alias="Count", description="Specifies maximum number of samples in the snapshot to return. Maximum is 1200. If not specified a default of 1200 samples are returned.")
    DataCurrency: Optional[str] = Field(default=None, alias="DataCurrency", description="Currency conversion in which data is expected in growth.")
    DataSeriesType: Optional[DataSeriesType] = Field(default=None, alias="DataSeriesType", description="Growth or Price | Growth in case of mutual funds and Price in case of other asset classes like Fx.")
    FieldGroups: Optional[List[ChartFieldGroupSpec]] = Field(default=None, alias="FieldGroups", description="Use FieldGroups to add additional information to the snapshot samples like display/formatting details or information about the price source. If FieldGroups are not specified in the request then the response defaults to only hold the bare OHLC samples and nothing else.")
    Horizon: Optional[int] = Field(default=None, alias="Horizon", description="The time period that each sample covers. Values are interpreted in minutes: 1, 2, 3, 5, 10, 15, 30, 60, 120, 180, 240, 300, 360, 480, 1440, 10080, 43200, 129600, 518400.")
    Uic: Optional[int] = Field(default=None, alias="Uic", description="Uic of the instrument.")

class CreateasubscriptiononchartdataRequest(_FlexModel):
    Arguments: Optional[ChartSubscriptionRequest] = Field(default=None, alias="Arguments", description="Arguments for the subscription request.")
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The streaming context id that this request is associated with. This parameter must only contain letters (a-z) and numbers (0-9) as well as - (dash) and _ (underscore). It is case insensitive. Max length is 50 characters.")
    Format: Optional[str] = Field(default=None, alias="Format", description="Optional Media type (RFC 2046) of the serialized data updates that are streamed to the client. Currently only application/json and application/x-protobuf is supported. If an unrecognized format is specified, the subscription end point will return HTTP status code 400 - Bad format.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="Mandatory client specified reference id for the subscription. This parameter must only contain alphanumberic characters as well as - (dash) and _ (underscore). Cannot start with _. It is case insensitive. Max length is 50 characters.")
    RefreshRate: Optional[int] = Field(default=None, alias="RefreshRate", description="Optional custom refresh rate, measured in milliseconds, between each data update. Note that it is not possible to get a refresh rate lower than the rate specified in the customer service level agreement (SLA).")
    ReplaceReferenceId: Optional[str] = Field(default=None, alias="ReplaceReferenceId", description="Reference id of the subscription that should be replaced.")
    Tag_Obsolete: Optional[str] = Field(default=None, alias="Tag Obsolete", description=": Optional client specified tag used for grouping subscriptions.")

class RemovemultiplesubscriptionsRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="Unique streaming context ID part of the streaming session.")
    Tag: Optional[str] = Field(default=None, alias="Tag", description="Tag that subscriptions are marked with.")

class RemovesubscriptionRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="Unique streaming context ID part of the streaming session.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="The reference id that identifies the subscription (within a streaming session).")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
