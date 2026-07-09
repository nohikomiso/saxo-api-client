"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class ManagementType(_FlexModel):
    Client: Optional[Any] = Field(default=None, alias="Client", description="The account is managed by the client. (Default).")
    ExternallyManaged: Optional[Any] = Field(default=None, alias="ExternallyManaged", description="The account is managed externally (not in a saxo bank system). Client cannot trade on the account, but authorized dealers can.")
    ModelAdvisory: Optional[Any] = Field(default=None, alias="ModelAdvisory", description="The account is managed by a model, but client has to accept changes to the model.")
    ModelManaged: Optional[Any] = Field(default=None, alias="ModelManaged", description="The account is managed by a model. Client cannot trade on the account.")
    SelfPeriodicInvestment: Optional[Any] = Field(default=None, alias="SelfPeriodicInvestment", description="Client can schedule periodic investments on one or multiple Instruments")
    TradeAdvisory: Optional[Any] = Field(default=None, alias="TradeAdvisory", description="Advisors can call clients with trade suggestions across products, but trades are accepted by the client.")

class GetclientholdingsRequest(_FlexModel):
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="Account group identifier")
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Account identifier")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Client identifier")
    EventId: Optional[str] = Field(default=None, alias="EventId", description="Event id")
    IncludeSubAccounts: Optional[bool] = Field(default=None, alias="IncludeSubAccounts", description="Indicate whether to include events from sub-clients.")
    ManagementTypes: Optional[List[ManagementType]] = Field(default=None, alias="ManagementTypes", description="SaxoInternal - Management type filter for holdings.")
    ModelIds: Optional[List[str]] = Field(default=None, alias="ModelIds", description="SaxoInternal - Model filter for holdings. Accepts comma separated model ids for filtering.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
