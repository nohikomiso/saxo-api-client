"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class ActivityType(_FlexModel):
    AccountDepreciation: Optional[Any] = Field(default=None, alias="AccountDepreciation", description="Account depreciation information.")
    AccountFundings: Optional[Any] = Field(default=None, alias="AccountFundings", description="Funding Information.")
    AdvisoryModelRebalance: Optional[Any] = Field(default=None, alias="AdvisoryModelRebalance", description="Advisory model rebalance related information.")
    CorporateActions: Optional[Any] = Field(default=None, alias="CorporateActions", description="Corporate action information")
    MarginCalls: Optional[Any] = Field(default=None, alias="MarginCalls", description="Margin call information.")
    Orders: Optional[Any] = Field(default=None, alias="Orders", description="Order related information.")
    PositionDepreciation: Optional[Any] = Field(default=None, alias="PositionDepreciation", description="Position Depreciation information.")
    Positions: Optional[Any] = Field(default=None, alias="Positions", description="Position related information.")
    SecurityTransfers: Optional[Any] = Field(default=None, alias="SecurityTransfers", description="Security Transfer related information.")

class CANotificationType(_FlexModel):
    Announcement: Optional[Any] = Field(default=None, alias="Announcement", description="Corporate action announcement.")
    Payment: Optional[Any] = Field(default=None, alias="Payment", description="Corporate action payment.")
    Update: Optional[Any] = Field(default=None, alias="Update", description="Corporate action update.")

class CorporateActionEventType(_FlexModel):
    Dividend: Optional[Any] = Field(default=None, alias="Dividend", description="Divivdends")
    NonDividend: Optional[Any] = Field(default=None, alias="NonDividend", description="Non-dividends")

class CorporateActionType(_FlexModel):
    Mandatory: Optional[Any] = Field(default=None, alias="Mandatory", description="Mandatory event")
    Voluntary: Optional[Any] = Field(default=None, alias="Voluntary", description="Voluntary event")

class OpenOrderDuration(_FlexModel):
    AtTheClose: Optional[Any] = Field(default=None, alias="AtTheClose", description="Working at the closing auction only")
    AtTheOpening: Optional[Any] = Field(default=None, alias="AtTheOpening", description="Working at the opening auction only")
    DayOrder: Optional[Any] = Field(default=None, alias="DayOrder", description="Day order - working in all session until trade date roll")
    FillOrKill: Optional[Any] = Field(default=None, alias="FillOrKill", description="Fill or kill")
    GoodForPeriod: Optional[Any] = Field(default=None, alias="GoodForPeriod", description="Working for specified period")
    GoodTillCancel: Optional[Any] = Field(default=None, alias="GoodTillCancel", description="Good Till Cancel - working until explicitly cancelled")
    GoodTillDate: Optional[Any] = Field(default=None, alias="GoodTillDate", description="Working untill specified date")
    ImmediateOrCancel: Optional[Any] = Field(default=None, alias="ImmediateOrCancel", description="Fill or fill partially and cancel remaining")
    Unknown: Optional[Any] = Field(default=None, alias="Unknown", description="Unspecified duration")

class ActivityFieldGroup(_FlexModel):
    DisplayAndFormat: Optional[Any] = Field(default=None, alias="DisplayAndFormat", description="Display and Format.")
    ExchangeInfo: Optional[Any] = Field(default=None, alias="ExchangeInfo", description="Adds information about the instrument's exchange.")

class OrderStatus(_FlexModel):
    Cancelled: Optional[Any] = Field(default=None, alias="Cancelled", description="Order cancelled.")
    Changed: Optional[Any] = Field(default=None, alias="Changed", description="Order changed.")
    DoneForDay: Optional[Any] = Field(default=None, alias="DoneForDay", description="Order is done for day.")
    Expired: Optional[Any] = Field(default=None, alias="Expired", description="Order expired.")
    Fill: Optional[Any] = Field(default=None, alias="Fill", description="Received fill on order.")
    FinalFill: Optional[Any] = Field(default=None, alias="FinalFill", description="Received final fill on order.")
    Parked: Optional[Any] = Field(default=None, alias="Parked", description="Order is Parked. Only applicable if 'Parked Order' functionality is configured for partner.")
    Placed: Optional[Any] = Field(default=None, alias="Placed", description="Order placed.")
    TrailingStopOrderMove: Optional[Any] = Field(default=None, alias="TrailingStopOrderMove", description="Movement in trailing Stop Order")

class OrderSubStatus(_FlexModel):
    Confirmed: Optional[Any] = Field(default=None, alias="Confirmed", description="Order confirmed.")
    Rejected: Optional[Any] = Field(default=None, alias="Rejected", description="Order rejected.")
    Requested: Optional[Any] = Field(default=None, alias="Requested", description="Order requested.")
    WaitCondition: Optional[Any] = Field(default=None, alias="WaitCondition", description="Order in wait condition.")

class PlaceableOrderType(_FlexModel):
    Algorithmic: Optional[Any] = Field(default=None, alias="Algorithmic", description="Algorithmic order type")
    DealCapture: Optional[Any] = Field(default=None, alias="DealCapture", description="Deal Capture Order. Specify to capture trades, which are already registered on Exchange, into Saxo System. Currently supported for selected partners only.")
    GuaranteedStop: Optional[Any] = Field(default=None, alias="GuaranteedStop", description="GuaranteedStop order type")
    Limit: Optional[Any] = Field(default=None, alias="Limit", description="Limit order type")
    Market: Optional[Any] = Field(default=None, alias="Market", description="Market order type")
    PreviouslyQuoted: Optional[Any] = Field(default=None, alias="PreviouslyQuoted", description="Previously quoted order type")
    Stop: Optional[Any] = Field(default=None, alias="Stop", description="Stop order type")
    StopIfTraded: Optional[Any] = Field(default=None, alias="StopIfTraded", description="StopIfTraded order type")
    StopLimit: Optional[Any] = Field(default=None, alias="StopLimit", description="StopLimit order type")
    Switch: Optional[Any] = Field(default=None, alias="Switch", description="Switch order type")
    TrailingStop: Optional[Any] = Field(default=None, alias="TrailingStop", description="Trailingstop order type")
    TrailingStopIfTraded: Optional[Any] = Field(default=None, alias="TrailingStopIfTraded", description="TrailingStopIfTraded order type")
    Traspaso: Optional[Any] = Field(default=None, alias="Traspaso", description="Traspaso order type")
    TraspasoIn: Optional[Any] = Field(default=None, alias="TraspasoIn", description="TrasapasoIn order type")
    TriggerBreakout: Optional[Any] = Field(default=None, alias="TriggerBreakout", description="A Breakout Order (Trigger order with up and down prices)")
    TriggerLimit: Optional[Any] = Field(default=None, alias="TriggerLimit", description="Similar to Limit order type but used only with Trigger orders")
    TriggerStop: Optional[Any] = Field(default=None, alias="TriggerStop", description="Similar to Stop order type but used only with Trigger orders")

class PositionEventFilter(_FlexModel):
    All: Optional[Any] = Field(default=None, alias="All", description="All positions events.")
    TradesOnly: Optional[Any] = Field(default=None, alias="TradesOnly", description="Positions events related fills or allocations.")

class GetactivitiesforspecifiedclientAccountRequest(_FlexModel):
    skiptoken: Optional[str] = Field(default=None, alias="$skiptoken", description="Specifies an entity id to start retrieving entries from. This is normally only used in generated nextlinks.")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="account group key for accounts used in retrieving the trade data. If specified, activities of the specified account will be returned/published otherwise activities of all accounts represented by ClientKey.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Unique key identifying the account used in retrieving the trade data. If specified, activities of the specified account will be returned/published otherwise activities of all accounts represented by ClientKey.")
    Activities: Optional[List[ActivityType]] = Field(default=None, alias="Activities", description="Specification of activity types to return in results.")
    CANotificationTypes: Optional[List[CANotificationType]] = Field(default=None, alias="CANotificationTypes", description="Corporate action notification type to get the response for.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique key identifying the client. If specified, activities of the specified client will be returned/published otherwise for logged in client.")
    CorporateActionEventTypes: Optional[List[CorporateActionEventType]] = Field(default=None, alias="CorporateActionEventTypes", description="Corporate Action Event type")
    CorporateActionTypes: Optional[List[CorporateActionType]] = Field(default=None, alias="CorporateActionTypes", description="Specify corporate action category, if any.")
    Duration: Optional[OpenOrderDuration] = Field(default=None, alias="Duration", description="The order duration type.")
    ExpirationDateTime: Optional[Any] = Field(default=None, alias="ExpirationDateTime", description="The expiration date should only be set if the duration type is GoodTillDate.")
    FieldGroups: Optional[List[ActivityFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specification of field groups to return in results.")
    FromDateTime: Optional[Any] = Field(default=None, alias="FromDateTime", description="If specified, activities starting FromDateTime will be returned/published. Default returns current day activities")
    IncludeSubAccounts: Optional[bool] = Field(default=None, alias="IncludeSubAccounts", description="If specified true, activities of sub-clients will also be returned/published.")
    OrderStatuses: Optional[List[OrderStatus]] = Field(default=None, alias="OrderStatuses", description="List of order statuses.")
    OrderSubStatuses: Optional[List[OrderSubStatus]] = Field(default=None, alias="OrderSubStatuses", description="List of order sub statuses.")
    OrderTypes: Optional[List[PlaceableOrderType]] = Field(default=None, alias="OrderTypes", description="List of order types.")
    PositionEventFilter: Optional[PositionEventFilter] = Field(default=None, alias="PositionEventFilter", description="Specify position event filter if any. Default is PositionEventFilter.All.")
    SequenceId: Optional[str] = Field(default=None, alias="SequenceId", description="If specified and message with SequenceId available in ENS cache, streaming of events start from SequenceId. If sequenceId not found in ENS system, Subscription Error with 'Sequence id unavailable' If not specified and FromDateTime is not specified, subscription will be real-time subscription.")
    SourceOrderId: Optional[str] = Field(default=None, alias="SourceOrderId", description="OrderId filter for activity types Orders and Positions.")
    TimeOnMargin: Optional[str] = Field(default=None, alias="TimeOnMargin", description="Time the client has been on margin. If specified, margin activities with greater or equal to the time specified otherwise all activities.")
    ToDateTime: Optional[Any] = Field(default=None, alias="ToDateTime", description="If specified, activities ending ToDateTime will be returned/published.")

class CorporateActionEventFilter(_FlexModel):
    CANotificationTypes: Optional[List[CANotificationType]] = Field(default=None, alias="CANotificationTypes", description="List of corporate action notification types.")
    CorporateActionEventTypes: Optional[List[CorporateActionEventType]] = Field(default=None, alias="CorporateActionEventTypes", description="Corporate Action Event type")
    CorporateActionTypes: Optional[List[CorporateActionType]] = Field(default=None, alias="CorporateActionTypes", description="Specify corporate action category, if any.")

class OrderDuration(_FlexModel):
    DurationType: Optional[OpenOrderDuration] = Field(default=None, alias="DurationType", description="The order duration type.")
    ExpirationDate: Optional[Any] = Field(default=None, alias="ExpirationDate", description="The expiration date, should only be set if the duration type is GoodTillDate.")
    ExpirationDateContainsTime: Optional[bool] = Field(default=None, alias="ExpirationDateContainsTime", description="The value indicating whether the ExpirationDateTime field contains the time. Notice, that the value can only be true for GoodTillDate duration type and the time must be provided in the ExpirationDateTime.")
    ExpirationDateTime: Optional[Any] = Field(default=None, alias="ExpirationDateTime", description="The expiration date (and optionally time), should only be set if the duration type is GoodTillDate. If the field contains the time, it must always be expressed in the exchange local time and the ExpirationDateContainsTime property must me set to true. Time zone indication must never be added. The time part should be in the following format: HH:mm, where HH is 24 hour clock. Seconds and milliseconds are not allowed.")
    ExpiryTimeOnExchange_Obsolete: Optional[str] = Field(default=None, alias="ExpiryTimeOnExchange Obsolete", description="The field has been obsoleted and has no effect. Use ExpirationDateTime and ExpirationDateContainsTime instead.")

class OrderEventFilter(_FlexModel):
    Duration: Optional[OrderDuration] = Field(default=None, alias="Duration", description="Order duration")
    OrderStatuses: Optional[List[OrderStatus]] = Field(default=None, alias="OrderStatuses", description="List of order statuses.")
    OrderSubStatuses: Optional[List[OrderSubStatus]] = Field(default=None, alias="OrderSubStatuses", description="List of order sub statuses.")
    OrderTypes: Optional[List[PlaceableOrderType]] = Field(default=None, alias="OrderTypes", description="List of order types.")

class SubscriptionActivityRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="account group key for accounts used in retrieving the trade data. If specified, activities of the specified account will be returned/published otherwise activities of all accounts represented by ClientKey.")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Unique key identifying the account used in retrieving the trade data. If specified, activities of the specified account will be returned/published otherwise activities of all accounts represented by ClientKey.")
    Activities: Optional[List[ActivityType]] = Field(default=None, alias="Activities", description="Specification of activity types to return in results.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique key identifying the client. If specified, activities of the specified client will be returned/published otherwise for logged in client.")
    CorporateActionEventFilter: Optional[CorporateActionEventFilter] = Field(default=None, alias="CorporateActionEventFilter", description="Specify corporate action event filter, if any.")
    FieldGroups: Optional[List[ActivityFieldGroup]] = Field(default=None, alias="FieldGroups", description="Specification of field groups to return in results.")
    FromDateTime: Optional[Any] = Field(default=None, alias="FromDateTime", description="If specified, activities starting FromDateTime will be returned/published. Default returns current day activities")
    IncludeSubAccounts: Optional[bool] = Field(default=None, alias="IncludeSubAccounts", description="If specified true, activities of sub-clients will also be returned/published.")
    OrderEventFilter: Optional[OrderEventFilter] = Field(default=None, alias="OrderEventFilter", description="Specify order event filter if any.")
    PositionEventFilter: Optional[PositionEventFilter] = Field(default=None, alias="PositionEventFilter", description="Specify position event filter if any. Default is PositionEventFilter.All.")
    SequenceId: Optional[str] = Field(default=None, alias="SequenceId", description="If specified and message with SequenceId available in ENS cache, streaming of events start from SequenceId. If sequenceId not found in ENS system, Subscription Error with 'Sequence id unavailable' If not specified and FromDateTime is not specified, subscription will be real-time subscription.")
    TimeOnMargin: Optional[str] = Field(default=None, alias="TimeOnMargin", description="Time the client has been on margin. If specified, margin activities with greater or equal to the time specified otherwise all activities.")
    ToDateTime: Optional[Any] = Field(default=None, alias="ToDateTime", description="If specified, activities ending ToDateTime will be returned/published.")

class CreateasubscriptionforclienteventsRequest(_FlexModel):
    Arguments: Optional[SubscriptionActivityRequest] = Field(default=None, alias="Arguments", description="Arguments for the subscription request.")
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The streaming context id that this request is associated with. This parameter must only contain letters (a-z) and numbers (0-9) as well as - (dash) and _ (underscore). It is case insensitive. Max length is 50 characters.")
    Format: Optional[str] = Field(default=None, alias="Format", description="Optional Media type (RFC 2046) of the serialized data updates that are streamed to the client. Currently only application/json and application/x-protobuf is supported. If an unrecognized format is specified, the subscription end point will return HTTP status code 400 - Bad format.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="Mandatory client specified reference id for the subscription. This parameter must only contain alphanumberic characters as well as - (dash) and _ (underscore). Cannot start with _. It is case insensitive. Max length is 50 characters.")
    RefreshRate: Optional[int] = Field(default=None, alias="RefreshRate", description="Optional custom refresh rate, measured in milliseconds, between each data update. Note that it is not possible to get a refresh rate lower than the rate specified in the customer service level agreement (SLA).")
    ReplaceReferenceId: Optional[str] = Field(default=None, alias="ReplaceReferenceId", description="Reference id of the subscription that should be replaced.")
    Tag_Obsolete: Optional[str] = Field(default=None, alias="Tag Obsolete", description=": Optional client specified tag used for grouping subscriptions.")

class RemovemultiplesubscriptionsRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The context id part of the streaming session (used to identify the subscription within a streaming session).")
    Tag: Optional[str] = Field(default=None, alias="Tag", description="Optional. Remove only subscriptions that are marked with specified tag.")

class RemovesubscriptionRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="Unique streaming context ID part of the streaming session.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="Unique ID of the subscription")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
