"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class PackagingEventData(_FlexModel):
    ExternalId: Optional[str] = Field(default=None, alias="ExternalId", description="This id refers to the tracking id provided during the creation of the signing session, which is used for internal correlation purposes.")
    Id: Optional[str] = Field(default=None, alias="Id", description="The signing sessions id related to signing session.")

class WebhooktonotifythecompletionoftheeSigningpackagingprocessRequest(_FlexModel):
    AccountId: Optional[str] = Field(default=None, alias="AccountId", description="The account ID which the event is sent in the context of")
    EventData: Optional[PackagingEventData] = Field(default=None, alias="EventData", description="The date related to the event.")
    EventName: Optional[str] = Field(default=None, alias="EventName", description="The name of the received event. The value for this event should be :- 'package.completed'.")
    ExpiresAt: Optional[str] = Field(default=None, alias="ExpiresAt", description="The timestamp when the event expires.")
    Id: Optional[str] = Field(default=None, alias="Id", description="Represents the unique identifier for the packaging complete event.")
    IsMockEvent: Optional[bool] = Field(default=None, alias="IsMockEvent", description="Gets or sets a value indicating whether the event is a mock event. Helpful for testing purposes.")
    Sender: Optional[str] = Field(default=None, alias="Sender", description="The service at the vendor's side that is sending the notification.")
    Tags: Optional[List[str]] = Field(default=None, alias="Tags", description="Optional tags that can be included in the event.")
    Timestamp: Optional[str] = Field(default=None, alias="Timestamp", description="The timestamp indicating when the packaging complete event was created.")

class WebhooktonotifythefailureoftheeSigningpackagingprocessRequest(_FlexModel):
    AccountId: Optional[str] = Field(default=None, alias="AccountId", description="The account ID which the event is sent in the context of")
    EventData: Optional[PackagingEventData] = Field(default=None, alias="EventData", description="The date related to the event.")
    EventName: Optional[str] = Field(default=None, alias="EventName", description="The name of the received event. The value for this event should be :- 'package.failed'.")
    ExpiresAt: Optional[str] = Field(default=None, alias="ExpiresAt", description="The timestamp when the event expires.")
    Id: Optional[str] = Field(default=None, alias="Id", description="Represents the unique identifier for the packaging complete event.")
    IsMockEvent: Optional[bool] = Field(default=None, alias="IsMockEvent", description="Gets or sets a value indicating whether the event is a mock event. Helpful for testing purposes.")
    Sender: Optional[str] = Field(default=None, alias="Sender", description="The service at the vendor's side that is sending the notification.")
    Tags: Optional[List[str]] = Field(default=None, alias="Tags", description="Optional tags that can be included in the event.")
    Timestamp: Optional[str] = Field(default=None, alias="Timestamp", description="The timestamp indicating when the packaging complete event was created.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
