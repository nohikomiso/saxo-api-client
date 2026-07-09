"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class ClosedPositionFieldGroup(_FlexModel):
    ClosedPosition: Optional[Any] = Field(default=None, alias="ClosedPosition", description="Closed position data which is calculated differently whether viewed at client or account level")
    ClosedPositionDetails: Optional[Any] = Field(default=None, alias="ClosedPositionDetails", description="Detailed information about a closed position. Applicable when ClosedPositionId is included in the request and not a subscription request.")
    DisplayAndFormat: Optional[Any] = Field(default=None, alias="DisplayAndFormat", description="Information about the instrument of the net position and how to display it.")
    ExchangeInfo: Optional[Any] = Field(default=None, alias="ExchangeInfo", description="Adds information about the instrument's exchange. This includes Exchange name, exchange code and open status.")

class GetclosedpositionsforaclientaccountGrouporaccountRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the closed positions belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The key of the account to which the closed positions belongs.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the closesd positions belongs.")
    ClosedPositionId: Optional[str] = Field(default=None, alias="ClosedPositionId", description="The id of the closed position to which the closedposition belongs")
    FieldGroups: Optional[List[ClosedPositionFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specifies which data to return. Default is [ClosedPosition]")

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

class BuySell(_FlexModel):
    Buy: Optional[Any] = Field(default=None, alias="Buy", description="Buy.")
    Sell: Optional[Any] = Field(default=None, alias="Sell", description="Sell.")

class PositionClosingMethod(_FlexModel):
    Explicit: Optional[Any] = Field(default=None, alias="Explicit", description="Explicit closed")
    Fifo: Optional[Any] = Field(default=None, alias="Fifo", description="Netting Closed")
    Unknown: Optional[Any] = Field(default=None, alias="Unknown", description="Unknown")

class ExpiryCut(_FlexModel):
    Budapest: Optional[Any] = Field(default=None, alias="Budapest", description="BD: Option is expired/exercised manually. Priced as NY.")
    Mexico: Optional[Any] = Field(default=None, alias="Mexico", description="Mexico cut (MX): Option is expired/exercised manually. Priced as NY.")
    Moscow: Optional[Any] = Field(default=None, alias="Moscow", description="Moscow cut (MW): Option is expired/exercised manually. Priced as NY.")
    None_: Optional[Any] = Field(default=None, alias="None", description="Not specified. Usually option trade with this type of expiration has invalid state or not initialized.")
    NY: Optional[Any] = Field(default=None, alias="NY", description="Option will be expired on the New-York time.")
    PreciousMetals: Optional[Any] = Field(default=None, alias="PreciousMetals", description="Precious metals cut (PM): Option is expired/exercised manually. Priced as NY.")
    TK: Optional[Any] = Field(default=None, alias="TK", description="Option will be expired on the Tokyo time.")
    Turkey: Optional[Any] = Field(default=None, alias="Turkey", description="Turkish cut (TR): Option is expired/exercised manually. Priced as NY.")
    Unknown: Optional[Any] = Field(default=None, alias="Unknown", description="Unknown cut: (UX): Option is expired/exercised manually. Priced as NY.")
    Warsaw: Optional[Any] = Field(default=None, alias="Warsaw", description="WR: Option is expired/exercised manually. Priced as NY.")

class PutCall(_FlexModel):
    Call: Optional[Any] = Field(default=None, alias="Call", description="Call.")
    None_: Optional[Any] = Field(default=None, alias="None", description="Not specified.")
    Put: Optional[Any] = Field(default=None, alias="Put", description="Put.")

class FXOptionsBaseData(_FlexModel):
    BarrierEventOccurred: Optional[bool] = Field(default=None, alias="BarrierEventOccurred", description="True if the barrier event has occurred for the option")
    ExpiryCut: Optional[ExpiryCut] = Field(default=None, alias="ExpiryCut", description="ExpiryCut.")
    ExpiryDate: Optional[Any] = Field(default=None, alias="ExpiryDate", description="The ExpiryDate.")
    LowerBarrier: Optional[float] = Field(default=None, alias="LowerBarrier", description="LowerBarrier for digital option.")
    PutCall: Optional[PutCall] = Field(default=None, alias="PutCall", description="The Put/Call value of the option.")
    Strike: Optional[float] = Field(default=None, alias="Strike", description="The strike price of the option.")
    UpperBarrier: Optional[float] = Field(default=None, alias="UpperBarrier", description="UpperBarrier for digital option.")

class ClosedPosition(_FlexModel):
    AccountId: Optional[str] = Field(default=None, alias="AccountId", description="The id of the account to which the closed position belongs.")
    Amount: Optional[float] = Field(default=None, alias="Amount", description="Sum volume of positions in instrument.")
    AssetType: Optional[AssetType] = Field(default=None, alias="AssetType", description="The AssetType.")
    BuyOrSell: Optional[BuySell] = Field(default=None, alias="BuyOrSell", description="Closing direction - Buy or Sell")
    ClientId: Optional[str] = Field(default=None, alias="ClientId", description="The id of the client to which the closed position belongs.")
    ClosedProfitLoss: Optional[float] = Field(default=None, alias="ClosedProfitLoss", description="Closed ProfitLoss in Instrument currency")
    ClosedProfitLossInBaseCurrency: Optional[float] = Field(default=None, alias="ClosedProfitLossInBaseCurrency", description="Closed ProfitLoss in Base (client/ account) currency")
    ClosingBondPoolFactor: Optional[float] = Field(default=None, alias="ClosingBondPoolFactor", description="The pool factor is a metric used to determine the proportion of the original principal that remains outstanding in a bond that is callable or redeemable before its maturity date. It is essential for calculating the actual initial principal amount left to pay to the client.")
    ClosingExternalReferenceId: Optional[str] = Field(default=None, alias="ClosingExternalReferenceId", description="Gets or sets the Client order reference id.")
    ClosingIndexRatio: Optional[float] = Field(default=None, alias="ClosingIndexRatio", description="Closing IndexRatio, Applicable for Inflation linked bonds.")
    ClosingMarketValue: Optional[float] = Field(default=None, alias="ClosingMarketValue", description="Market value at closing for non-options in instrument currency")
    ClosingMarketValueInBaseCurrency: Optional[float] = Field(default=None, alias="ClosingMarketValueInBaseCurrency", description="Market value at closing for non-options in base currency")
    ClosingMethod: Optional[PositionClosingMethod] = Field(default=None, alias="ClosingMethod", description="The closing method of the position. Possible values: Explicit, Fifo.")
    ClosingPositionId: Optional[str] = Field(default=None, alias="ClosingPositionId", description="The Id of closing position that caused closing..")
    ClosingPremium: Optional[float] = Field(default=None, alias="ClosingPremium", description="Premium for option positions that are closed, in instrument currency")
    ClosingPremiumInBaseCurrency: Optional[float] = Field(default=None, alias="ClosingPremiumInBaseCurrency", description="Premium for option positions that are closed, in base currency")
    ClosingPrice: Optional[float] = Field(default=None, alias="ClosingPrice", description="Closing price")
    ConversionRateInstrumentToBaseSettledClosing: Optional[bool] = Field(default=None, alias="ConversionRateInstrumentToBaseSettledClosing", description="True when the closing trades currency conversion rate has been settled (i.e. is fixed and not fluctuating). This is the case for accounts using Market Conversion-Rates.")
    ConversionRateInstrumentToBaseSettledOpening: Optional[bool] = Field(default=None, alias="ConversionRateInstrumentToBaseSettledOpening", description="True when the opening trades currency conversion rate has been settled (i.e. is fixed and not fluctuating). This is the case for accounts using Market Conversion-Rates.")
    CostClosing: Optional[float] = Field(default=None, alias="CostClosing", description="Total Cost in instrument currency")
    CostClosingInBaseCurrency: Optional[float] = Field(default=None, alias="CostClosingInBaseCurrency", description="Total Cost in client/account currency")
    CostOpening: Optional[float] = Field(default=None, alias="CostOpening", description="Total Cost in instrument currency")
    CostOpeningInBaseCurrency: Optional[float] = Field(default=None, alias="CostOpeningInBaseCurrency", description="Total Cost in client/account currency")
    ExecutionTimeClose: Optional[Any] = Field(default=None, alias="ExecutionTimeClose", description="The UTC date and time the position was closed.")
    ExecutionTimeOpen: Optional[Any] = Field(default=None, alias="ExecutionTimeOpen", description="The UTC date and time the position was opened.")
    ExpiryDate: Optional[Any] = Field(default=None, alias="ExpiryDate", description="The ExpiryDate.")
    FxOptionData: Optional[FXOptionsBaseData] = Field(default=None, alias="FxOptionData", description="Fx option-related data. Only for fx options.")
    NoticeDate: Optional[Any] = Field(default=None, alias="NoticeDate", description="Futures only - The date on which the owner may be required to take physical delivery of the instrument commodity.")
    OpeningBondPoolFactor: Optional[float] = Field(default=None, alias="OpeningBondPoolFactor", description="Volume Weighted Open Pool Factor for Non-Inflation-Linked-Bonds is an average measure of the remaining principal of these bonds, weighted by their volume.")
    OpeningExternalReferenceId: Optional[str] = Field(default=None, alias="OpeningExternalReferenceId", description="Gets or sets the Client order reference id.")
    OpeningIndexRatio: Optional[float] = Field(default=None, alias="OpeningIndexRatio", description="Opening IndexRatio, Applicable for Inflation linked bonds.")
    OpeningPositionId: Optional[str] = Field(default=None, alias="OpeningPositionId", description="The Id of opening position that has been closed.")
    OpenPrice: Optional[float] = Field(default=None, alias="OpenPrice", description="The price the instrument was traded at.")
    ProfitLossCurrencyConversion: Optional[float] = Field(default=None, alias="ProfitLossCurrencyConversion", description="The profit loss from currency conversion between position close and position open.")
    ProfitLossOnTrade: Optional[float] = Field(default=None, alias="ProfitLossOnTrade", description="The P/L on the trade in the currency in which the instrument is traded.")
    ProfitLossOnTradeInBaseCurrency: Optional[float] = Field(default=None, alias="ProfitLossOnTradeInBaseCurrency", description="The P/L in the client/account group/account currency.")
    SrdSettlementDate: Optional[Any] = Field(default=None, alias="SrdSettlementDate", description="SRD Settlement Date")
    Uic: Optional[int] = Field(default=None, alias="Uic", description="Unique id of the instrument.")

class PriceDisplayFormatType(_FlexModel):
    AllowDecimalPips: Optional[Any] = Field(default=None, alias="AllowDecimalPips", description="Display the last digit as a smaller than the rest of the numbers. Note that this digit is not included in the number of decimals, effectively increasing the number of decimals by one. E.g. 12.345 when Decimals is 2 and DisplayFormat is AllowDecimalPips.")
    Fractions: Optional[Any] = Field(default=None, alias="Fractions", description="Display as regular fraction i.e. 3 1/4")
    ModernFractions: Optional[Any] = Field(default=None, alias="ModernFractions", description="Special US Bonds futures fractional format (1/32s or 1/128s without nominator). If PriceDecimals = -5 then the nominator is 32, else 128.")
    Normal: Optional[Any] = Field(default=None, alias="Normal", description="Standard decimal formatting is used with the Decimals field indicating the number of decimals.")
    Percentage: Optional[Any] = Field(default=None, alias="Percentage", description="Display as percentage, e.g. 12.34%.")

class DisplayHintType(_FlexModel):
    Continuous: Optional[Any] = Field(default=None, alias="Continuous", description="Used for the parent ContractFutures.")
    CryptoCurrencies: Optional[Any] = Field(default=None, alias="CryptoCurrencies", description="Crypto Currencies. Intended to be used for Forex Spot / crypto currency crosses..")
    Forex: Optional[Any] = Field(default=None, alias="Forex", description="Forex. Intended to be used for Cfds on Futures on Forex.")
    Interests: Optional[Any] = Field(default=None, alias="Interests", description="Interest rates. Intended to be used for Cfds on Futures on bonds.")
    None_: Optional[Any] = Field(default=None, alias="None", description="Indicates not special display hint is required.")
    PreciousMetal: Optional[Any] = Field(default=None, alias="PreciousMetal", description="Metals like XAUUSD.")
    StockIndices: Optional[Any] = Field(default=None, alias="StockIndices", description="Stock indices. Intended to be used for Cfds on Futures on stock indices.")

class InstrumentDisplayAndFormat(_FlexModel):
    BarrierDecimals: Optional[int] = Field(default=None, alias="BarrierDecimals", description="Number of display decimals for barrier price. One touch/no touch options only.")
    BarrierFormat: Optional[PriceDisplayFormatType] = Field(default=None, alias="BarrierFormat", description="Display format of barrier price. One touch/no touch options only.")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="The ISO currency code of the instrument.")
    Decimals: Optional[int] = Field(default=None, alias="Decimals", description="The resolution in which e.g. a price must be displayed and possibly edited. Positive numbers are represents digits, and negative numbers represent fractions using this formula: 1/(2^x). Same as DisplayDecimals.")
    Description: Optional[str] = Field(default=None, alias="Description", description="Description of instrument (DAX Index - Nov 2013), in English.")
    DisplayHint: Optional[DisplayHintType] = Field(default=None, alias="DisplayHint", description="Hint to the client application about how it should display the instrument.")
    Format: Optional[PriceDisplayFormatType] = Field(default=None, alias="Format", description="Format code specifying how price should be formatted.")
    NumeratorDecimals: Optional[int] = Field(default=None, alias="NumeratorDecimals", description="Some fractional prices have decimals in the numerator, e.g. 2.5/32. This is relevant for futures and cfds on futures.")
    OrderDecimals: Optional[int] = Field(default=None, alias="OrderDecimals", description="The number of decimals trigger price for orders should be formatted with.")
    StrikeDecimals: Optional[int] = Field(default=None, alias="StrikeDecimals", description="The decimals value to use when formatting strike price. Only relevant for options.")
    StrikeFormat: Optional[PriceDisplayFormatType] = Field(default=None, alias="StrikeFormat", description="The price format to use when formatting strike price. Only relevant for options.")
    Symbol: Optional[str] = Field(default=None, alias="Symbol", description="Symbol- A combination of letters used to uniquely identify a traded instrument. e.g. ODAX/X13C8950:xeur.")
    UnderlyingInstrumentDescription_Obsolete: Optional[str] = Field(default=None, alias="UnderlyingInstrumentDescription Obsolete", description="Common full name of the underlying instrument. Only used for options and is the same as the option root description.")

class InstrumentExchangeDetails(_FlexModel):
    Description: Optional[str] = Field(default=None, alias="Description", description="Full name/description of the exchange")
    ExchangeId: Optional[str] = Field(default=None, alias="ExchangeId", description="Short exchange code.")
    IsOpen: Optional[bool] = Field(default=None, alias="IsOpen", description="Indicates if the exchange is currently open for trading")
    TimeZoneId: Optional[str] = Field(default=None, alias="TimeZoneId", description="Exchange's TimeZone")

class ClosedPositionResponse(_FlexModel):
    ClosedPosition: Optional[ClosedPosition] = Field(default=None, alias="ClosedPosition", description="ClosedPosition info")
    ClosedPositionUniqueId: Optional[str] = Field(default=None, alias="ClosedPositionUniqueId", description="Unique id of the closed position based on OpeningPositionId and ClosingPositionId - Required for subscription to provide a key.")
    DisplayAndFormat: Optional[InstrumentDisplayAndFormat] = Field(default=None, alias="DisplayAndFormat", description="[Community] Information about the instrument of the closed position and how to display it.")
    Exchange: Optional[InstrumentExchangeDetails] = Field(default=None, alias="Exchange", description="Information about the instrument's exchange and trading status.")
    NetPositionId: Optional[str] = Field(default=None, alias="NetPositionId", description="NetPosition ID")

class GetclosedpositionsforaclientaccountGrouporaccountResponse(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[ClosedPositionResponse]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")

class GetasinglepositionRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the closed positions belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The key of the account to which the closed positions belongs.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the closesd positions belongs.")
    ClosedPositionId: Optional[str] = Field(default=None, alias="ClosedPositionId", description="Unique id of the position.")
    FieldGroups: Optional[List[ClosedPositionFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specifies which data to return. Default is [ClosedPosition]")

class GetasinglepositionResponse(_FlexModel):
    ClosedPosition: Optional[ClosedPosition] = Field(default=None, alias="ClosedPosition", description="ClosedPosition info")
    ClosedPositionUniqueId: Optional[str] = Field(default=None, alias="ClosedPositionUniqueId", description="Unique id of the closed position based on OpeningPositionId and ClosingPositionId - Required for subscription to provide a key.")
    DisplayAndFormat: Optional[InstrumentDisplayAndFormat] = Field(default=None, alias="DisplayAndFormat", description="[Community] Information about the instrument of the closed position and how to display it.")
    Exchange: Optional[InstrumentExchangeDetails] = Field(default=None, alias="Exchange", description="Information about the instrument's exchange and trading status.")
    NetPositionId: Optional[str] = Field(default=None, alias="NetPositionId", description="NetPosition ID")

class GetclosedpositionsforaclienttowhichtheloggedinuserbelongsRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    FieldGroups: Optional[List[ClosedPositionFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specifies which data to return. Default is [ClosedPosition].")

class GetclosedpositionsforaclienttowhichtheloggedinuserbelongsResponse(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[ClosedPositionResponse]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")

class ClosedPositionRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="The key of the account group to which the closed positions belongs.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The key of the account to which the closed positions belongs.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the closesd positions belongs.")
    ClosedPositionId: Optional[str] = Field(default=None, alias="ClosedPositionId", description="The id of the closed position to which the closedposition belongs")
    FieldGroups: Optional[List[ClosedPositionFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specifies which data to return. Default is [ClosedPosition]")

class CreateasubscriptiononalistofclosedpositionsandmakeitactiveRequest(_FlexModel):
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    Arguments: Optional[ClosedPositionRequest] = Field(default=None, alias="Arguments", description="Arguments for the subscription request.")
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The streaming context id that this request is associated with. This parameter must only contain letters (a-z) and numbers (0-9) as well as - (dash) and _ (underscore). It is case insensitive. Max length is 50 characters.")
    Format: Optional[str] = Field(default=None, alias="Format", description="Optional Media type (RFC 2046) of the serialized data updates that are streamed to the client. Currently only application/json and application/x-protobuf is supported. If an unrecognized format is specified, the subscription end point will return HTTP status code 400 - Bad format.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="Mandatory client specified reference id for the subscription. This parameter must only contain alphanumberic characters as well as - (dash) and _ (underscore). Cannot start with _. It is case insensitive. Max length is 50 characters.")
    RefreshRate: Optional[int] = Field(default=None, alias="RefreshRate", description="Optional custom refresh rate, measured in milliseconds, between each data update. Note that it is not possible to get a refresh rate lower than the rate specified in the customer service level agreement (SLA).")
    ReplaceReferenceId: Optional[str] = Field(default=None, alias="ReplaceReferenceId", description="Reference id of the subscription that should be replaced.")
    Tag_Obsolete: Optional[str] = Field(default=None, alias="Tag Obsolete", description=": Optional client specified tag used for grouping subscriptions.")

class ClosedPositionResponseListResult(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[ClosedPositionResponse]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")

class CreateasubscriptiononalistofclosedpositionsandmakeitactiveResponse(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The streaming context id that this response is associated with.")
    Format: Optional[str] = Field(default=None, alias="Format", description="The media type (RFC 2046), of the serialized data updates that are streamed to the client.")
    InactivityTimeout: Optional[int] = Field(default=None, alias="InactivityTimeout", description="The time (in seconds) that the client should accept the subscription to be inactive before considering it invalid.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="The reference id that (along with streaming context id and session id) identifies the subscription (within the context of a specific service/subscription type)")
    RefreshRate: Optional[int] = Field(default=None, alias="RefreshRate", description="Actual refresh rate assigned to the subscription according to the customers SLA.")
    Snapshot: Optional[ClosedPositionResponseListResult] = Field(default=None, alias="Snapshot", description="Snapshot of the current data on hand, when subscription was created.")
    State: Optional[str] = Field(default=None, alias="State", description="This property is kept for backwards compatibility.")
    Tag_Obsolete: Optional[str] = Field(default=None, alias="Tag Obsolete", description=": Client specified tag assigned to the subscription, if specified in the request.")
    ClosedPosition: Optional[ClosedPosition] = Field(default=None, alias="ClosedPosition", description="ClosedPosition info")
    ClosedPositionUniqueId: Optional[str] = Field(default=None, alias="ClosedPositionUniqueId", description="Unique id of the closed position based on OpeningPositionId and ClosingPositionId - Required for subscription to provide a key.")
    DisplayAndFormat: Optional[InstrumentDisplayAndFormat] = Field(default=None, alias="DisplayAndFormat", description="[Community] Information about the instrument of the closed position and how to display it.")
    Exchange: Optional[InstrumentExchangeDetails] = Field(default=None, alias="Exchange", description="Information about the instrument's exchange and trading status.")
    NetPositionId: Optional[str] = Field(default=None, alias="NetPositionId", description="NetPosition ID")

class RemovemultiplesubscriptionsRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The context id part of the streaming session (used to identify the subscription within a streaming session).")
    Tag: Optional[str] = Field(default=None, alias="Tag", description="Optional. Remove only subscriptions that are marked with specified tag.")

class ChangetheclosedpositionssubscriptionpagesizeRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The context id part of the streaming session.")
    NewPageSize: Optional[int] = Field(default=None, alias="NewPageSize", description="Extends or reduces the page size, number of positions shown, on a running positions subscription.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="Unique ID of the subscription")

class RemovesubscriptionRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The context id part of the streaming session (used to identify the subscription within a streaming session).")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="Unique id of the subscription")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
