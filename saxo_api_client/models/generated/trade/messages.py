"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class MessageDisplayType(_FlexModel):
    Default: Optional[Any] = Field(default=None, alias="Default", description="No message render method is set.")
    Popup: Optional[Any] = Field(default=None, alias="Popup", description="Message is to popup suggesting immediate attention")

class TradeMessageType(_FlexModel):
    AccountDepreciation: Optional[Any] = Field(default=None, alias="AccountDepreciation", description="Message to indicate that an account has depreciated beyond a limit as specified by MIFID II regulations. Only sent for configured client segments.")
    MarginCall: Optional[Any] = Field(default=None, alias="MarginCall", description="A margin call is a message informing the client about loses affecting his ability fulfill the margin requirements of his positions in the market.")
    Mifid: Optional[Any] = Field(default=None, alias="Mifid", description="A change has been made to the clients Mifid classification. Only sent for configured client segments.")
    Notification: Optional[Any] = Field(default=None, alias="Notification", description="Message from broker to end client")
    PositionDepreciation: Optional[Any] = Field(default=None, alias="PositionDepreciation", description="Message to indicate that a position has depreciated beyond a limit as specified by MIFID II regulations. Only sent for configured client segments.")
    PriceAlert: Optional[Any] = Field(default=None, alias="PriceAlert", description="A price alert has been triggered")
    ShareWorkspaceNotification: Optional[Any] = Field(default=None, alias="ShareWorkspaceNotification", description="Platform Workspace Notification: Share workspace notification")
    TradeConfirmation: Optional[Any] = Field(default=None, alias="TradeConfirmation", description="A very broad set of notifications related to orders and positions. For example: * An order has been placed * An order has expired * An order has been (partially) filled * An order was cancelled * A position was stopped out (due to insufficient margin) * A position was placed")

class TradeMessageResponse(_FlexModel):
    DateTime: Optional[Any] = Field(default=None, alias="DateTime", description="Date and Time the message was generated.")
    DisplayType: Optional[MessageDisplayType] = Field(default=None, alias="DisplayType", description="Suggestion to the application about how the message should be displayed.")
    MessageBody: Optional[str] = Field(default=None, alias="MessageBody", description="Trade message body. This is fully formatted text in the language selected for the logged in client.")
    MessageHeader: Optional[str] = Field(default=None, alias="MessageHeader", description="Header of the message")
    MessageId: Optional[str] = Field(default=None, alias="MessageId", description="Unique identification of the message")
    MessageType: Optional[TradeMessageType] = Field(default=None, alias="MessageType", description="The type of the message.")

class GettrademessagesforthecurrentuserRequest(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[TradeMessageResponse]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")

class MarktrademessageasseenRequest(_FlexModel):
    MessageIds: Optional[List[str]] = Field(default=None, alias="MessageIds", description="Unique ids of the message.")

class CreateasubscriptionontrademessagesRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="The streaming context id that this request is associated with. This parameter must only contain letters (a-z) and numbers (0-9) as well as - (dash) and _ (underscore). It is case insensitive. Max length is 50 characters.")
    Format: Optional[str] = Field(default=None, alias="Format", description="Optional Media type (RFC 2046) of the serialized data updates that are streamed to the client. Currently only application/json and application/x-protobuf is supported. If an unrecognized format is specified, the subscription end point will return HTTP status code 400 - Bad format.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="Mandatory client specified reference id for the subscription. This parameter must only contain alphanumberic characters as well as - (dash) and _ (underscore). Cannot start with _. It is case insensitive. Max length is 50 characters.")
    RefreshRate: Optional[int] = Field(default=None, alias="RefreshRate", description="Optional custom refresh rate, measured in milliseconds, between each data update. Note that it is not possible to get a refresh rate lower than the rate specified in the customer service level agreement (SLA).")
    ReplaceReferenceId: Optional[str] = Field(default=None, alias="ReplaceReferenceId", description="Reference id of the subscription that should be replaced.")
    Tag_Obsolete: Optional[str] = Field(default=None, alias="Tag Obsolete", description=": Optional client specified tag used for grouping subscriptions.")

class RemovemultipletrademessagesubscriptionsRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="Unique streaming context ID part of the streaming session.")
    Tag: Optional[str] = Field(default=None, alias="Tag", description="The tag which the subscriptions are grouped under.")

class RemoveatrademessagesubscriptionRequest(_FlexModel):
    ContextId: Optional[str] = Field(default=None, alias="ContextId", description="Unique streaming context ID part of the streaming session.")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="Unique reference ID of the subscription to remove.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
