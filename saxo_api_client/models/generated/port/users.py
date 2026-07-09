"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class ActiveUsersFilter(_FlexModel):
    Active: Optional[Any] = Field(default=None, alias="Active", description="Active users")
    All: Optional[Any] = Field(default=None, alias="All", description="Active and inactive users")
    Inactive: Optional[Any] = Field(default=None, alias="Inactive", description="Inactive users")

class GetallusersunderaparticularownerRequest(_FlexModel):
    inlinecount: Optional[str] = Field(default=None, alias="$inlinecount", description="Specifies that the response to the request should include a count of the number of entries in the collection")
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    ActiveUsersFilter: Optional[ActiveUsersFilter] = Field(default=None, alias="ActiveUsersFilter", description="Optional. Controls what users to be included in terms of active/inactive. Default is all users.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique key identifying the owner. This is the ClientKey of the client under which the list of users belongs. Default: Logged-in user's client.")
    IncludeSubUsers: Optional[bool] = Field(default=None, alias="IncludeSubUsers", description="Optional. Set to true if users of all underlying partners should be included in output.")

class LoginStatus(_FlexModel):
    Successful: Optional[Any] = Field(default=None, alias="Successful", description="The user logged in")
    Unsuccessful: Optional[Any] = Field(default=None, alias="Unsuccessful", description="The user recieved an access denied")

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

class UserResponse(_FlexModel):
    Active: Optional[bool] = Field(default=None, alias="Active", description="Whether the user is active.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique key identifying the client that owns the user.")
    Culture: Optional[str] = Field(default=None, alias="Culture", description="Selected culture for this user. Five letter language culture name. Fx. en-GB")
    Language: Optional[str] = Field(default=None, alias="Language", description="Selected language for this user. The two letter ISO 639-1 language code. See Reference Data Languages endpoint for supported languages.")
    LastLoginStatus: Optional[LoginStatus] = Field(default=None, alias="LastLoginStatus", description="Status of last login or login attempt")
    LastLoginTime: Optional[Any] = Field(default=None, alias="LastLoginTime", description="Time of last login or login attempt")
    LegalAssetTypes: Optional[List[AssetType]] = Field(default=None, alias="LegalAssetTypes", description="Asset Types that can be traded on all accounts by this user.")
    MarketDataViaOpenApiTermsAccepted: Optional[bool] = Field(default=None, alias="MarketDataViaOpenApiTermsAccepted", description="True if the user has accepted terms for market data via OpenApi access.")
    Name: Optional[str] = Field(default=None, alias="Name", description="The name of the user.")
    TimeZoneId: Optional[int] = Field(default=None, alias="TimeZoneId", description="Selected Time Zone for this user. See Reference Data TimeZones endpoint for supported time zones.")
    UserId: Optional[str] = Field(default=None, alias="UserId", description="Unique ID of the user.")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="The unique key for the user.")

class GetallusersunderaparticularownerResponse(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[UserResponse]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")

class GetthedetailsaboutauserRequest(_FlexModel):
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="The unique key for the user's client.")

class GetthedetailsaboutauserResponse(_FlexModel):
    Active: Optional[bool] = Field(default=None, alias="Active", description="Whether the user is active.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique key identifying the client that owns the user.")
    Culture: Optional[str] = Field(default=None, alias="Culture", description="Selected culture for this user. Five letter language culture name. Fx. en-GB")
    Language: Optional[str] = Field(default=None, alias="Language", description="Selected language for this user. The two letter ISO 639-1 language code. See Reference Data Languages endpoint for supported languages.")
    LastLoginStatus: Optional[LoginStatus] = Field(default=None, alias="LastLoginStatus", description="Status of last login or login attempt")
    LastLoginTime: Optional[Any] = Field(default=None, alias="LastLoginTime", description="Time of last login or login attempt")
    LegalAssetTypes: Optional[List[AssetType]] = Field(default=None, alias="LegalAssetTypes", description="Asset Types that can be traded on all accounts by this user.")
    MarketDataViaOpenApiTermsAccepted: Optional[bool] = Field(default=None, alias="MarketDataViaOpenApiTermsAccepted", description="True if the user has accepted terms for market data via OpenApi access.")
    Name: Optional[str] = Field(default=None, alias="Name", description="The name of the user.")
    TimeZoneId: Optional[int] = Field(default=None, alias="TimeZoneId", description="Selected Time Zone for this user. See Reference Data TimeZones endpoint for supported time zones.")
    UserId: Optional[str] = Field(default=None, alias="UserId", description="Unique ID of the user.")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="The unique key for the user.")

class EntitlementFieldSet(_FlexModel):
    Default: Optional[Any] = Field(default=None, alias="Default", description="Return the AssetTypes in the Entitlements array where user has real time access on prices.")
    IncludeDelayed: Optional[Any] = Field(default=None, alias="IncludeDelayed", description="Return the AssetTypes in the Entitlements array where user has real time and delayed access on prices.")

class GetallentitlementsaboutauserRequest(_FlexModel):
    EntitlementFieldSet: Optional[EntitlementFieldSet] = Field(default=None, alias="EntitlementFieldSet", description="Specifies which values to be returned in the Entitlements array.")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="The unique key for the user's client.")

class Entitlement(_FlexModel):
    DelayedFullBook: Optional[List[AssetType]] = Field(default=None, alias="DelayedFullBook", description="AssetTypes where user has delayed top of book access on prices.")
    DelayedGreeks: Optional[List[AssetType]] = Field(default=None, alias="DelayedGreeks", description="AssetTypes where user has delayed access on greeks.")
    Greeks: Optional[List[AssetType]] = Field(default=None, alias="Greeks", description="AssetTypes where user has real time access on greeks.")
    RealTimeFullBook: Optional[List[AssetType]] = Field(default=None, alias="RealTimeFullBook", description="AssetTypes where user has real time full book access on prices.")
    RealTimeTopOfBook: Optional[List[AssetType]] = Field(default=None, alias="RealTimeTopOfBook", description="AssetTypes where user has real time top of book access on prices.")

class GetallentitlementsaboutauserResponse(_FlexModel):
    Entitlements: Optional[List[Entitlement]] = Field(default=None, alias="Entitlements", description="The all client specific entitlements for market data, which the user currently has access to..")
    ExchangeId: Optional[str] = Field(default=None, alias="ExchangeId", description="The unique ID of the exchange.")

class GetdetailsabouttheloggedinuserResponse(_FlexModel):
    Active: Optional[bool] = Field(default=None, alias="Active", description="Whether the user is active.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique key identifying the client that owns the user.")
    Culture: Optional[str] = Field(default=None, alias="Culture", description="Selected culture for this user. Five letter language culture name. Fx. en-GB")
    Language: Optional[str] = Field(default=None, alias="Language", description="Selected language for this user. The two letter ISO 639-1 language code. See Reference Data Languages endpoint for supported languages.")
    LastLoginStatus: Optional[LoginStatus] = Field(default=None, alias="LastLoginStatus", description="Status of last login or login attempt")
    LastLoginTime: Optional[Any] = Field(default=None, alias="LastLoginTime", description="Time of last login or login attempt")
    LegalAssetTypes: Optional[List[AssetType]] = Field(default=None, alias="LegalAssetTypes", description="Asset Types that can be traded on all accounts by this user.")
    MarketDataViaOpenApiTermsAccepted: Optional[bool] = Field(default=None, alias="MarketDataViaOpenApiTermsAccepted", description="True if the user has accepted terms for market data via OpenApi access.")
    Name: Optional[str] = Field(default=None, alias="Name", description="The name of the user.")
    TimeZoneId: Optional[int] = Field(default=None, alias="TimeZoneId", description="Selected Time Zone for this user. See Reference Data TimeZones endpoint for supported time zones.")
    UserId: Optional[str] = Field(default=None, alias="UserId", description="Unique ID of the user.")
    UserKey: Optional[Any] = Field(default=None, alias="UserKey", description="The unique key for the user.")

class UpdateuserpreferencesRequest(_FlexModel):
    Culture: Optional[str] = Field(default=None, alias="Culture", description="Selected culture for this user. Five letter language culture name. Fx. en-GB")
    Language: Optional[str] = Field(default=None, alias="Language", description="Selected language for this user. The two letter ISO 639-1 language code. See Reference Data Languages endpoint for supported languages.")
    TimeZoneId: Optional[int] = Field(default=None, alias="TimeZoneId", description="Selected Time Zone for this user. See Reference Data TimeZones endpoint for supported time zones.")

class GetallentitlementsRequest(_FlexModel):
    EntitlementFieldSet: Optional[EntitlementFieldSet] = Field(default=None, alias="EntitlementFieldSet", description="")

class EntitlementDetails(_FlexModel):
    Entitlements: Optional[List[Entitlement]] = Field(default=None, alias="Entitlements", description="The all client specific entitlements for market data, which the user currently has access to..")
    ExchangeId: Optional[str] = Field(default=None, alias="ExchangeId", description="The unique ID of the exchange.")

class GetallentitlementsResponse(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[EntitlementDetails]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
