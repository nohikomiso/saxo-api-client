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

class Class(_FlexModel):
    Complex: Optional[Any] = Field(default=None, alias="Complex", description="Complex")
    NonComplex: Optional[Any] = Field(default=None, alias="NonComplex", description="Non-complex")

class SearchforinstrumentsorcontractoptionrootsRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="If specified, access permissions to instruments for the specified account will be evaluated. Optional.")
    AssetTypes: Optional[List[AssetType]] = Field(default=None, alias="AssetTypes", description="Comma separated list of one or more asset types to search for. E.g. AssetTypes=FxSpot,Stock")
    CanParticipateInMultiLegOrder: Optional[bool] = Field(default=None, alias="CanParticipateInMultiLegOrder", description="Should the result only include option roots that allow/disallow exchange traded option strategies, also know as multi-leg or combination orders. All roots are returned regardless if omitted.")
    Class: Optional[List[Class]] = Field(default=None, alias="Class", description="The class of the instruments to include in the search.")
    ExchangeId: Optional[str] = Field(default=None, alias="ExchangeId", description="ID of the exchange that the instruments must match.")
    IncludeNonTradable: Optional[bool] = Field(default=None, alias="IncludeNonTradable", description="Should the search include instruments, which are not online client tradable?")
    Keywords: Optional[str] = Field(default=None, alias="Keywords", description="Search for matching keywords in the instruments. Separate keywords with spaces.")
    OneMonthTotalValueChangesFrom: Optional[float] = Field(default=None, alias="OneMonthTotalValueChangesFrom", description="Subject to data license agreements. Upper filter boundary for one month total value changes that the instruments must match.")
    OneMonthTotalValueChangesTo: Optional[float] = Field(default=None, alias="OneMonthTotalValueChangesTo", description="Subject to data license agreements. Lower filter boundary for one month total value changes that the instruments must match.")
    OneWeekTotalValueChangesFrom: Optional[float] = Field(default=None, alias="OneWeekTotalValueChangesFrom", description="Subject to data license agreements. Upper filter boundary for one week total value changes that the instruments must match.")
    OneWeekTotalValueChangesTo: Optional[float] = Field(default=None, alias="OneWeekTotalValueChangesTo", description="Subject to data license agreements. Lower filter boundary for one week total value changes that the instruments must match.")
    OneYearTotalValueChangesFrom: Optional[float] = Field(default=None, alias="OneYearTotalValueChangesFrom", description="Subject to data license agreements. Upper filter boundary for one year total value changes that the instruments must match.")
    OneYearTotalValueChangesTo: Optional[float] = Field(default=None, alias="OneYearTotalValueChangesTo", description="Subject to data license agreements. Lower filter boundary for one year total value changes that the instruments must match.")
    Tags: Optional[List[str]] = Field(default=None, alias="Tags", description="Allows filtering by display hint, on Stocks, ETFs and ETCs are currently supported. Use null to indicate Tag should not be included in search criteria. Currently only one tag is supported.")
    Uics: Optional[List[int]] = Field(default=None, alias="Uics", description="Limit list to return information for the following Uics")

class OptionSpaceSegment(_FlexModel):
    AllDates: Optional[Any] = Field(default=None, alias="AllDates", description="Return complete option space.")
    DefaultDates: Optional[Any] = Field(default=None, alias="DefaultDates", description="Return all options for the 'default' days.")
    None_: Optional[Any] = Field(default=None, alias="None", description="Do not include the option space.")
    SpecificDates: Optional[Any] = Field(default=None, alias="SpecificDates", description="Return all options for specified strike days.")
    UnderlyingUic: Optional[Any] = Field(default=None, alias="UnderlyingUic", description="Used to specify filter to return all options for with specified underlying Uic.")

class TradingStatus(_FlexModel):
    NonTradable: Optional[Any] = Field(default=None, alias="NonTradable", description="Instrument is non tradable")
    NotDefined: Optional[Any] = Field(default=None, alias="NotDefined", description="Not Defined")
    ReduceOnly: Optional[Any] = Field(default=None, alias="ReduceOnly", description="Instrument is Reduce only, which means client can only reduce the exposure by closing existing open position(s) and cannot open new position(s).")
    Tradable: Optional[Any] = Field(default=None, alias="Tradable", description="Instrument is tradable")

class GetoptiondetailsandoptionsspaceforspecifiedoptionrootRequest(_FlexModel):
    CanParticipateInMultiLegOrder: Optional[bool] = Field(default=None, alias="CanParticipateInMultiLegOrder", description="Should the result only include option roots that allow/disallow exchange traded option strategies, also know as multi-leg or combination orders. This is an optional parameter, all roots are returned regardless if omitted.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    ExpiryDates: Optional[List[str]] = Field(default=None, alias="ExpiryDates", description="Return specific information for the ExpiryDates in this array (if OptionSpaceSegment is set to 'SpecificDates').")
    OptionRootId: Optional[int] = Field(default=None, alias="OptionRootId", description="ID of the contract option root.")
    OptionSpaceSegment: Optional[OptionSpaceSegment] = Field(default=None, alias="OptionSpaceSegment", description="How large a segment of the option space should return full contract option details (in the OptionsSpace[].SpecificOptions property). Default is None.")
    TradingStatus: Optional[TradingStatus] = Field(default=None, alias="TradingStatus", description="")
    UnderlyingUic: Optional[int] = Field(default=None, alias="UnderlyingUic", description="The uic of the underlying instrument. This is an optional parameter (if OptionSpaceSegment is set to 'UnderlyingUic').")

class InstrumentFieldGroup(_FlexModel):
    OrderSetting: Optional[Any] = Field(default=None, alias="OrderSetting", description="Adds information about the instrument's order setting.")
    SupportedOrderTypeSettings: Optional[Any] = Field(default=None, alias="SupportedOrderTypeSettings", description="Adds information about supported order types.")
    TradingSessions: Optional[Any] = Field(default=None, alias="TradingSessions", description="Adds information about the instrument's trading sessions.")

class GetdetailedinformationforlistofinstrumentsRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="If specified, access permissions to instruments for the specified account will be evaluated. Optional.")
    AssetTypes: Optional[List[AssetType]] = Field(default=None, alias="AssetTypes", description="Comma separated list of one or more asset types to search for. E.g. AssetTypes=FxSpot,Stock")
    FieldGroups: Optional[List[InstrumentFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specifies comma-separated list of additional fields to receive.")
    Tags: Optional[List[str]] = Field(default=None, alias="Tags", description="Allows filtering by display hint, on Stocks, ETFs and ETCs are currently supported. Use null to indicate Tag should not be included in search criteria. Currently only one tag is supported.")
    Uics: Optional[List[int]] = Field(default=None, alias="Uics", description="Limit list to return information for the following Uics")

class GetdetailedinformationforaspecificinstrumentRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="")
    AssetType: Optional[AssetType] = Field(default=None, alias="AssetType", description="The of the instrument to get.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    FieldGroups: Optional[List[InstrumentFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specifies comma-separated list of additional fields to receive.")
    Uic: Optional[Any] = Field(default=None, alias="Uic", description="The Universal Instrument Code (UIC) of the instrument to get.")

class GetcontractfuturesspaceRequest(_FlexModel):
    ContinuousFuturesUic: Optional[int] = Field(default=None, alias="ContinuousFuturesUic", description="The UIC of the continuous futures instrument of the space.")

class TradingschedulesRequest(_FlexModel):
    AssetType: Optional[AssetType] = Field(default=None, alias="AssetType", description="The of the instrument to get.")
    Uic: Optional[Any] = Field(default=None, alias="Uic", description="The Universal Instrument Code (UIC) of the instrument to get.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
