"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetdetailsaboutclientsunderaparticularownerRequest(_FlexModel):
    inlinecount: Optional[str] = Field(default=None, alias="$inlinecount", description="Specifies that the response to the request should include a count of the number of entries in the collection")
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    OwnerKey: Optional[Any] = Field(default=None, alias="OwnerKey", description="Unique key identifying the owner. This is the clientKey of the client under which the list of clients belongs. Default: Logged-in user's client.")

class ClientPositionNettingProfile(_FlexModel):
    AverageRealTime: Optional[Any] = Field(default=None, alias="AverageRealTime", description="AverageRealTime netting profile")
    FifoEndOfDay: Optional[Any] = Field(default=None, alias="FifoEndOfDay", description="FifoEndOfDay netting profile")
    FifoRealTime: Optional[Any] = Field(default=None, alias="FifoRealTime", description="FifoRealTime netting profile")

class AllowedTradingSessions(_FlexModel):
    All: Optional[Any] = Field(default=None, alias="All", description="Extended trading hours session.")
    Regular: Optional[Any] = Field(default=None, alias="Regular", description="Default value. Regular trading hours session.")

class CollateralMonitoringMode(_FlexModel):
    CollateralCreditValue: Optional[Any] = Field(default=None, alias="CollateralCreditValue", description="Monitoring (stop-out's) are based on collateral credit value")
    MaxOfCollateralCreditValueAndCollateralCreditLine: Optional[Any] = Field(default=None, alias="MaxOfCollateralCreditValueAndCollateralCreditLine", description="Monitoring (stop-out's) are based on collateral credit value and collateral credit line.")

class ContractOptionsTradingProfile(_FlexModel):
    Advanced: Optional[Any] = Field(default=None, alias="Advanced", description="Can perform complex strategies.")
    Basic: Optional[Any] = Field(default=None, alias="Basic", description="Can perform basic options trading such as buying calls and puts.")
    Expert: Optional[Any] = Field(default=None, alias="Expert", description="Can perform all types of options trades and strategies.")
    None_: Optional[Any] = Field(default=None, alias="None", description="Not configured for options trading.")

class ClientContractType(_FlexModel):
    JointAccount: Optional[Any] = Field(default=None, alias="JointAccount", description="Joint account")

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

class PortfolioMarginMethod(_FlexModel):
    Default: Optional[Any] = Field(default=None, alias="Default", description="Uses Saxo exposure based margin.")
    JanusMarginReplication: Optional[Any] = Field(default=None, alias="JanusMarginReplication", description="Uses rules-based the Janus methodology to calculate margin.")
    SpanForFutures: Optional[Any] = Field(default=None, alias="SpanForFutures", description="Uses rules-based SPAN methods to calculate margin on futures alone.")
    SpanForFuturesAndOptions: Optional[Any] = Field(default=None, alias="SpanForFuturesAndOptions", description="Uses rules-based SPAN methods to calculate margin on futures and options.")

class MarginMonitoringMode(_FlexModel):
    Equity: Optional[Any] = Field(default=None, alias="Equity", description="Monitoring is based on standard equity utilization, pre-check's are done against standard equity utilization.")
    Lines: Optional[Any] = Field(default=None, alias="Lines", description="Monitoring (stop-out's) are based on credit line utilization, pre-check's are done against trading and credit line utilization.")
    Margin: Optional[Any] = Field(default=None, alias="Margin", description="Monitoring (stop-out's) are based on standard margin utilization, pre-check's are done against standard margin utilization.")

class MutualFundsCashAmountOrderCurrency(_FlexModel):
    Account: Optional[Any] = Field(default=None, alias="Account", description="Use the specified account currency.")
    Instrument: Optional[Any] = Field(default=None, alias="Instrument", description="Use the currency of the specified instrument.")

class ClientPositionNettingMethod(_FlexModel):
    Average: Optional[Any] = Field(default=None, alias="Average", description="Average Netting Method")
    FIFO: Optional[Any] = Field(default=None, alias="FIFO", description="FIFO Netting Method")

class ClientPositionNettingMode(_FlexModel):
    EndOfDay: Optional[Any] = Field(default=None, alias="EndOfDay", description="Default EndOfDay netting mode.")
    Intraday: Optional[Any] = Field(default=None, alias="Intraday", description="Intraday netting mode.")

class SecurityLendingEnabled(_FlexModel):
    No: Optional[Any] = Field(default=None, alias="No", description="Security Lending is disabled.")
    Yes: Optional[Any] = Field(default=None, alias="Yes", description="Security Lending is enabled.")

class ClientResponse(_FlexModel):
    AccountValueProtectionLimit: Optional[float] = Field(default=None, alias="AccountValueProtectionLimit", description="If set, this value shields the total client value from going below the given limit by automatically triggering closing of positions should the limit be exceeded. A limit of zero means there is no limit.")
    AllowedNettingProfiles: Optional[List[ClientPositionNettingProfile]] = Field(default=None, alias="AllowedNettingProfiles", description="Allowed Netting Profiles for Client.")
    AllowedTradingSessions: Optional[AllowedTradingSessions] = Field(default=None, alias="AllowedTradingSessions", description="Indicates if the client is allowed for extended trading hours.")
    ClientId: Optional[str] = Field(default=None, alias="ClientId", description="Unique ID of the client - for display to the user.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The unique key for the client.")
    CollateralMonitoringMode: Optional[CollateralMonitoringMode] = Field(default=None, alias="CollateralMonitoringMode", description="Collateral Monitoring Mode. Null when entity is not monitored on collateral.")
    ContractOptionsTradingProfile: Optional[ContractOptionsTradingProfile] = Field(default=None, alias="ContractOptionsTradingProfile", description="Specifies the contract options trading profile.")
    ContractType: Optional[ClientContractType] = Field(default=None, alias="ContractType", description="Client Contract Type. Null if Client contract doesn’t belong to joint account.")
    CurrencyDecimals: Optional[int] = Field(default=None, alias="CurrencyDecimals", description="Number of decimals used in currency.")
    DefaultAccountId: Optional[str] = Field(default=None, alias="DefaultAccountId", description="The default account for this client.")
    DefaultAccountKey: Optional[Any] = Field(default=None, alias="DefaultAccountKey", description="The unique key for the client's default account.")
    DefaultCurrency: Optional[str] = Field(default=None, alias="DefaultCurrency", description="The default currency for this client. Used for example for aggregation: if the client has accounts in multiple currencies, show the aggregated P/L in the this currency.")
    ForceOpenDefaultValue: Optional[bool] = Field(default=None, alias="ForceOpenDefaultValue", description="If True, the order(s) placed by default will be set to force open , therfore resulting positions will not automatically be netted with positions in the opposite direction.")
    IsMarginTradingAllowed: Optional[bool] = Field(default=None, alias="IsMarginTradingAllowed", description="Indicates whether trading on margin is allowed for the account.")
    IsVariationMarginEligible: Optional[bool] = Field(default=None, alias="IsVariationMarginEligible", description="Indicates if the client is enabled for withdrawal of unrealized profit/loss of derivatives positions.")
    LegalAssetTypes: Optional[List[AssetType]] = Field(default=None, alias="LegalAssetTypes", description="The combined list of asset types, which can be traded on at least one of the accounts owned by this client.")
    LegalAssetTypesAreIndicative: Optional[bool] = Field(default=None, alias="LegalAssetTypesAreIndicative", description="Certain clients have LegalAssetTypes on the account level and there may be instrument specific exceptions, so the client application must look up the individual instruments in Ref/InstrumentDetails to determine trade and prices permissions.")
    MarginCalculationMethod: Optional[PortfolioMarginMethod] = Field(default=None, alias="MarginCalculationMethod", description="Calculation method for assessing margin utilization.")
    MarginMonitoringMode: Optional[MarginMonitoringMode] = Field(default=None, alias="MarginMonitoringMode", description="Margin Monitoring Mode. Null when entity is not monitored on margin.")
    MutualFundsCashAmountOrderCurrency: Optional[MutualFundsCashAmountOrderCurrency] = Field(default=None, alias="MutualFundsCashAmountOrderCurrency", description="Indicates the currency used when placing MutualFunds orders with OrderAmountType.CashAmount.")
    Name: Optional[str] = Field(default=None, alias="Name", description="The name of the client.")
    PositionNettingMethod: Optional[ClientPositionNettingMethod] = Field(default=None, alias="PositionNettingMethod", description="The position netting method for this client.")
    PositionNettingMode: Optional[ClientPositionNettingMode] = Field(default=None, alias="PositionNettingMode", description="The position netting mode for this client.")
    PositionNettingProfile: Optional[ClientPositionNettingProfile] = Field(default=None, alias="PositionNettingProfile", description="The position netting profile for this client.")
    ReduceExposureOnly: Optional[bool] = Field(default=None, alias="ReduceExposureOnly", description="If True, Client has been marked to reduce exposure.")
    SecurityLendingEnabled: Optional[SecurityLendingEnabled] = Field(default=None, alias="SecurityLendingEnabled", description="Indicates if the client is enabled for security lending.")
    SupportsAccountValueProtectionLimit: Optional[bool] = Field(default=None, alias="SupportsAccountValueProtectionLimit", description="If true, an AccountValueProtectionLimit may be set on the client level. If it is false, the AccountValueProtectionLimit must be set on individual accounts or on account group level.")

class GetdetailsaboutclientsunderaparticularownerResponse(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[ClientResponse]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")

class EnablesIBtoswitchpositionnettingmodeornettingprofileandchangeAccountValueProtectionLimitRequest(_FlexModel):
    AccountValueProtectionLimit: Optional[float] = Field(default=None, alias="AccountValueProtectionLimit", description="If set, this value shields the total client value from going below the given limit by automatically triggering closing of positions should the limit be exceeded. A limit of zero means there is no limit.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="clientKey of the client that to switch.")
    ForceOpenDefaultValue: Optional[bool] = Field(default=None, alias="ForceOpenDefaultValue", description="If True, the order(s) placed by default will be set to force open , therfore resulting positions will not automatically be netted with positions in the opposite direction")
    NewPositionNettingMode: Optional[ClientPositionNettingMode] = Field(default=None, alias="NewPositionNettingMode", description="The position netting mode, client would like to switch to.")
    NewPositionNettingProfile: Optional[ClientPositionNettingProfile] = Field(default=None, alias="NewPositionNettingProfile", description="The position netting profile, client would like to switch to.")

class GetclientdetailsRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique key identifying the Client.")

class GetclientdetailsResponse(_FlexModel):
    AccountValueProtectionLimit: Optional[float] = Field(default=None, alias="AccountValueProtectionLimit", description="If set, this value shields the total client value from going below the given limit by automatically triggering closing of positions should the limit be exceeded. A limit of zero means there is no limit.")
    AllowedNettingProfiles: Optional[List[ClientPositionNettingProfile]] = Field(default=None, alias="AllowedNettingProfiles", description="Allowed Netting Profiles for Client.")
    AllowedTradingSessions: Optional[AllowedTradingSessions] = Field(default=None, alias="AllowedTradingSessions", description="Indicates if the client is allowed for extended trading hours.")
    ClientId: Optional[str] = Field(default=None, alias="ClientId", description="Unique ID of the client - for display to the user.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The unique key for the client.")
    CollateralMonitoringMode: Optional[CollateralMonitoringMode] = Field(default=None, alias="CollateralMonitoringMode", description="Collateral Monitoring Mode. Null when entity is not monitored on collateral.")
    ContractOptionsTradingProfile: Optional[ContractOptionsTradingProfile] = Field(default=None, alias="ContractOptionsTradingProfile", description="Specifies the contract options trading profile.")
    ContractType: Optional[ClientContractType] = Field(default=None, alias="ContractType", description="Client Contract Type. Null if Client contract doesn’t belong to joint account.")
    CurrencyDecimals: Optional[int] = Field(default=None, alias="CurrencyDecimals", description="Number of decimals used in currency.")
    DefaultAccountId: Optional[str] = Field(default=None, alias="DefaultAccountId", description="The default account for this client.")
    DefaultAccountKey: Optional[Any] = Field(default=None, alias="DefaultAccountKey", description="The unique key for the client's default account.")
    DefaultCurrency: Optional[str] = Field(default=None, alias="DefaultCurrency", description="The default currency for this client. Used for example for aggregation: if the client has accounts in multiple currencies, show the aggregated P/L in the this currency.")
    ForceOpenDefaultValue: Optional[bool] = Field(default=None, alias="ForceOpenDefaultValue", description="If True, the order(s) placed by default will be set to force open , therfore resulting positions will not automatically be netted with positions in the opposite direction.")
    IsMarginTradingAllowed: Optional[bool] = Field(default=None, alias="IsMarginTradingAllowed", description="Indicates whether trading on margin is allowed for the account.")
    IsVariationMarginEligible: Optional[bool] = Field(default=None, alias="IsVariationMarginEligible", description="Indicates if the client is enabled for withdrawal of unrealized profit/loss of derivatives positions.")
    LegalAssetTypes: Optional[List[AssetType]] = Field(default=None, alias="LegalAssetTypes", description="The combined list of asset types, which can be traded on at least one of the accounts owned by this client.")
    LegalAssetTypesAreIndicative: Optional[bool] = Field(default=None, alias="LegalAssetTypesAreIndicative", description="Certain clients have LegalAssetTypes on the account level and there may be instrument specific exceptions, so the client application must look up the individual instruments in Ref/InstrumentDetails to determine trade and prices permissions.")
    MarginCalculationMethod: Optional[PortfolioMarginMethod] = Field(default=None, alias="MarginCalculationMethod", description="Calculation method for assessing margin utilization.")
    MarginMonitoringMode: Optional[MarginMonitoringMode] = Field(default=None, alias="MarginMonitoringMode", description="Margin Monitoring Mode. Null when entity is not monitored on margin.")
    MutualFundsCashAmountOrderCurrency: Optional[MutualFundsCashAmountOrderCurrency] = Field(default=None, alias="MutualFundsCashAmountOrderCurrency", description="Indicates the currency used when placing MutualFunds orders with OrderAmountType.CashAmount.")
    Name: Optional[str] = Field(default=None, alias="Name", description="The name of the client.")
    PositionNettingMethod: Optional[ClientPositionNettingMethod] = Field(default=None, alias="PositionNettingMethod", description="The position netting method for this client.")
    PositionNettingMode: Optional[ClientPositionNettingMode] = Field(default=None, alias="PositionNettingMode", description="The position netting mode for this client.")
    PositionNettingProfile: Optional[ClientPositionNettingProfile] = Field(default=None, alias="PositionNettingProfile", description="The position netting profile for this client.")
    ReduceExposureOnly: Optional[bool] = Field(default=None, alias="ReduceExposureOnly", description="If True, Client has been marked to reduce exposure.")
    SecurityLendingEnabled: Optional[SecurityLendingEnabled] = Field(default=None, alias="SecurityLendingEnabled", description="Indicates if the client is enabled for security lending.")
    SupportsAccountValueProtectionLimit: Optional[bool] = Field(default=None, alias="SupportsAccountValueProtectionLimit", description="If true, an AccountValueProtectionLimit may be set on the client level. If it is false, the AccountValueProtectionLimit must be set on individual accounts or on account group level.")

class GetloggedinclientdetailsResponse(_FlexModel):
    AccountValueProtectionLimit: Optional[float] = Field(default=None, alias="AccountValueProtectionLimit", description="If set, this value shields the total client value from going below the given limit by automatically triggering closing of positions should the limit be exceeded. A limit of zero means there is no limit.")
    AllowedNettingProfiles: Optional[List[ClientPositionNettingProfile]] = Field(default=None, alias="AllowedNettingProfiles", description="Allowed Netting Profiles for Client.")
    AllowedTradingSessions: Optional[AllowedTradingSessions] = Field(default=None, alias="AllowedTradingSessions", description="Indicates if the client is allowed for extended trading hours.")
    ClientId: Optional[str] = Field(default=None, alias="ClientId", description="Unique ID of the client - for display to the user.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The unique key for the client.")
    CollateralMonitoringMode: Optional[CollateralMonitoringMode] = Field(default=None, alias="CollateralMonitoringMode", description="Collateral Monitoring Mode. Null when entity is not monitored on collateral.")
    ContractOptionsTradingProfile: Optional[ContractOptionsTradingProfile] = Field(default=None, alias="ContractOptionsTradingProfile", description="Specifies the contract options trading profile.")
    ContractType: Optional[ClientContractType] = Field(default=None, alias="ContractType", description="Client Contract Type. Null if Client contract doesn’t belong to joint account.")
    CurrencyDecimals: Optional[int] = Field(default=None, alias="CurrencyDecimals", description="Number of decimals used in currency.")
    DefaultAccountId: Optional[str] = Field(default=None, alias="DefaultAccountId", description="The default account for this client.")
    DefaultAccountKey: Optional[Any] = Field(default=None, alias="DefaultAccountKey", description="The unique key for the client's default account.")
    DefaultCurrency: Optional[str] = Field(default=None, alias="DefaultCurrency", description="The default currency for this client. Used for example for aggregation: if the client has accounts in multiple currencies, show the aggregated P/L in the this currency.")
    ForceOpenDefaultValue: Optional[bool] = Field(default=None, alias="ForceOpenDefaultValue", description="If True, the order(s) placed by default will be set to force open , therfore resulting positions will not automatically be netted with positions in the opposite direction.")
    IsMarginTradingAllowed: Optional[bool] = Field(default=None, alias="IsMarginTradingAllowed", description="Indicates whether trading on margin is allowed for the account.")
    IsVariationMarginEligible: Optional[bool] = Field(default=None, alias="IsVariationMarginEligible", description="Indicates if the client is enabled for withdrawal of unrealized profit/loss of derivatives positions.")
    LegalAssetTypes: Optional[List[AssetType]] = Field(default=None, alias="LegalAssetTypes", description="The combined list of asset types, which can be traded on at least one of the accounts owned by this client.")
    LegalAssetTypesAreIndicative: Optional[bool] = Field(default=None, alias="LegalAssetTypesAreIndicative", description="Certain clients have LegalAssetTypes on the account level and there may be instrument specific exceptions, so the client application must look up the individual instruments in Ref/InstrumentDetails to determine trade and prices permissions.")
    MarginCalculationMethod: Optional[PortfolioMarginMethod] = Field(default=None, alias="MarginCalculationMethod", description="Calculation method for assessing margin utilization.")
    MarginMonitoringMode: Optional[MarginMonitoringMode] = Field(default=None, alias="MarginMonitoringMode", description="Margin Monitoring Mode. Null when entity is not monitored on margin.")
    MutualFundsCashAmountOrderCurrency: Optional[MutualFundsCashAmountOrderCurrency] = Field(default=None, alias="MutualFundsCashAmountOrderCurrency", description="Indicates the currency used when placing MutualFunds orders with OrderAmountType.CashAmount.")
    Name: Optional[str] = Field(default=None, alias="Name", description="The name of the client.")
    PositionNettingMethod: Optional[ClientPositionNettingMethod] = Field(default=None, alias="PositionNettingMethod", description="The position netting method for this client.")
    PositionNettingMode: Optional[ClientPositionNettingMode] = Field(default=None, alias="PositionNettingMode", description="The position netting mode for this client.")
    PositionNettingProfile: Optional[ClientPositionNettingProfile] = Field(default=None, alias="PositionNettingProfile", description="The position netting profile for this client.")
    ReduceExposureOnly: Optional[bool] = Field(default=None, alias="ReduceExposureOnly", description="If True, Client has been marked to reduce exposure.")
    SecurityLendingEnabled: Optional[SecurityLendingEnabled] = Field(default=None, alias="SecurityLendingEnabled", description="Indicates if the client is enabled for security lending.")
    SupportsAccountValueProtectionLimit: Optional[bool] = Field(default=None, alias="SupportsAccountValueProtectionLimit", description="If true, an AccountValueProtectionLimit may be set on the client level. If it is false, the AccountValueProtectionLimit must be set on individual accounts or on account group level.")

class EnablesusertoswitchpositionnettingmodeornettingprofileRequest(_FlexModel):
    AccountValueProtectionLimit: Optional[float] = Field(default=None, alias="AccountValueProtectionLimit", description="If set, this value shields the total client value from going below the given limit by automatically triggering closing of positions should the limit be exceeded. A limit of zero means there is no limit.")
    ForceOpenDefaultValue: Optional[bool] = Field(default=None, alias="ForceOpenDefaultValue", description="If True, the order(s) placed by default will be set to force open , therfore resulting positions will not automatically be netted with positions in the opposite direction")
    NewPositionNettingMode: Optional[ClientPositionNettingMode] = Field(default=None, alias="NewPositionNettingMode", description="The position netting mode, client would like to switch to.")
    NewPositionNettingProfile: Optional[ClientPositionNettingProfile] = Field(default=None, alias="NewPositionNettingProfile", description="The position netting profile, client would like to switch to.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
