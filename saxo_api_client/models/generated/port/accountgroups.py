"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetalistofallaccountsgroupsusedbythespecifiedclientRequest(_FlexModel):
    inlinecount: Optional[str] = Field(default=None, alias="$inlinecount", description="Specifies that the response to the request should include a count of the number of entries in the collection")
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The client to which the account groups belong.")

class CollateralMonitoringMode(_FlexModel):
    CollateralCreditValue: Optional[Any] = Field(default=None, alias="CollateralCreditValue", description="Monitoring (stop-out's) are based on collateral credit value")
    MaxOfCollateralCreditValueAndCollateralCreditLine: Optional[Any] = Field(default=None, alias="MaxOfCollateralCreditValueAndCollateralCreditLine", description="Monitoring (stop-out's) are based on collateral credit value and collateral credit line.")

class PortfolioMarginMethod(_FlexModel):
    Default: Optional[Any] = Field(default=None, alias="Default", description="Uses Saxo exposure based margin.")
    JanusMarginReplication: Optional[Any] = Field(default=None, alias="JanusMarginReplication", description="Uses rules-based the Janus methodology to calculate margin.")
    SpanForFutures: Optional[Any] = Field(default=None, alias="SpanForFutures", description="Uses rules-based SPAN methods to calculate margin on futures alone.")
    SpanForFuturesAndOptions: Optional[Any] = Field(default=None, alias="SpanForFuturesAndOptions", description="Uses rules-based SPAN methods to calculate margin on futures and options.")

class MarginLendingEnabled(_FlexModel):
    No: Optional[Any] = Field(default=None, alias="No", description="Margin Lending is disabled.")
    None_: Optional[Any] = Field(default=None, alias="None", description="Default. Margin Lending is not applicable.")
    Yes: Optional[Any] = Field(default=None, alias="Yes", description="Margin Lending is enabled.")

class MarginMonitoringMode(_FlexModel):
    Equity: Optional[Any] = Field(default=None, alias="Equity", description="Monitoring is based on standard equity utilization, pre-check's are done against standard equity utilization.")
    Lines: Optional[Any] = Field(default=None, alias="Lines", description="Monitoring (stop-out's) are based on credit line utilization, pre-check's are done against trading and credit line utilization.")
    Margin: Optional[Any] = Field(default=None, alias="Margin", description="Monitoring (stop-out's) are based on standard margin utilization, pre-check's are done against standard margin utilization.")

class AccountGroupResponse(_FlexModel):
    AccountGroupId: Optional[str] = Field(default=None, alias="AccountGroupId", description="Unique ID of the account group")
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="Unique ID of the account group used for selection")
    AccountGroupName: Optional[str] = Field(default=None, alias="AccountGroupName", description="Name of the account group, displayed to the user")
    AccountValueProtectionLimit: Optional[float] = Field(default=None, alias="AccountValueProtectionLimit", description="If set, this value shields the account value from going below the given limit by automatically triggering closing of positions should the limit be exceeded. A limit of zero means there is no limit.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique ID of the client.")
    CollateralMonitoringMode: Optional[CollateralMonitoringMode] = Field(default=None, alias="CollateralMonitoringMode", description="Collateral Monitoring Mode. Null when entity is not monitored on collateral.")
    MarginCalculationMethod: Optional[PortfolioMarginMethod] = Field(default=None, alias="MarginCalculationMethod", description="Calculation method for assessing margin utilization.")
    MarginLendingEnabled: Optional[MarginLendingEnabled] = Field(default=None, alias="MarginLendingEnabled", description="Margin Lending Enabled")
    MarginMonitoringMode: Optional[MarginMonitoringMode] = Field(default=None, alias="MarginMonitoringMode", description="Margin Monitoring Mode. Null when entity is not monitored on margin.")
    PortfolioBasedMarginEnabled: Optional[bool] = Field(default=None, alias="PortfolioBasedMarginEnabled", description="Portfolio Based Margin (PBM) is a method for mapping the risk of an investment portfolio. True if enabled else false.")
    SupportsAccountValueProtectionLimit: Optional[bool] = Field(default=None, alias="SupportsAccountValueProtectionLimit", description="If true, an AccountValueProtectionLimit may be set on this account. If it is false, the AccountValueProtectionLimit can be set on client or account group.")

class GetalistofallaccountsgroupsusedbythespecifiedclientResponse(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[AccountGroupResponse]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")

class GetdetailsaboutasingleaccountgroupRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="Unique key for the account group.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the account group belong.")

class GetdetailsaboutasingleaccountgroupResponse(_FlexModel):
    AccountGroupId: Optional[str] = Field(default=None, alias="AccountGroupId", description="Unique ID of the account group")
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="Unique ID of the account group used for selection")
    AccountGroupName: Optional[str] = Field(default=None, alias="AccountGroupName", description="Name of the account group, displayed to the user")
    AccountValueProtectionLimit: Optional[float] = Field(default=None, alias="AccountValueProtectionLimit", description="If set, this value shields the account value from going below the given limit by automatically triggering closing of positions should the limit be exceeded. A limit of zero means there is no limit.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Unique ID of the client.")
    CollateralMonitoringMode: Optional[CollateralMonitoringMode] = Field(default=None, alias="CollateralMonitoringMode", description="Collateral Monitoring Mode. Null when entity is not monitored on collateral.")
    MarginCalculationMethod: Optional[PortfolioMarginMethod] = Field(default=None, alias="MarginCalculationMethod", description="Calculation method for assessing margin utilization.")
    MarginLendingEnabled: Optional[MarginLendingEnabled] = Field(default=None, alias="MarginLendingEnabled", description="Margin Lending Enabled")
    MarginMonitoringMode: Optional[MarginMonitoringMode] = Field(default=None, alias="MarginMonitoringMode", description="Margin Monitoring Mode. Null when entity is not monitored on margin.")
    PortfolioBasedMarginEnabled: Optional[bool] = Field(default=None, alias="PortfolioBasedMarginEnabled", description="Portfolio Based Margin (PBM) is a method for mapping the risk of an investment portfolio. True if enabled else false.")
    SupportsAccountValueProtectionLimit: Optional[bool] = Field(default=None, alias="SupportsAccountValueProtectionLimit", description="If true, an AccountValueProtectionLimit may be set on this account. If it is false, the AccountValueProtectionLimit can be set on client or account group.")

class UpdateaccountgroupinformationRequest(_FlexModel):
    AccountGroupKey: Optional[Any] = Field(default=None, alias="AccountGroupKey", description="Unique key of the account group to change.")
    AccountValueProtectionLimit: Optional[float] = Field(default=None, alias="AccountValueProtectionLimit", description="If set, this value shields the account value from going below the given limit by automatically triggering closing of positions should the limit be exceeded. A limit of zero means there is no limit.")
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="The key of the client to which the account group belong.")

class GetallaccountsgroupsunderaparticularclienttowhichtheloggedinuserbelongsRequest(_FlexModel):
    inlinecount: Optional[str] = Field(default=None, alias="$inlinecount", description="Specifies that the response to the request should include a count of the number of entries in the collection")
    skip: Optional[int] = Field(default=None, alias="$skip", description="The number of entries to skip from the beginning of the collection")
    top: Optional[int] = Field(default=None, alias="$top", description="The number of entries to return from the beginning of the collection")

class GetallaccountsgroupsunderaparticularclienttowhichtheloggedinuserbelongsResponse(_FlexModel):
    count: Optional[float] = Field(default=None, alias="__count", description="The total count of items in the feed.")
    next: Optional[str] = Field(default=None, alias="__next", description="The link for the next page of items in the feed.")
    Data: Optional[List[AccountGroupResponse]] = Field(default=None, alias="Data", description="The collection of entities for this feed.")
    MaxRows: Optional[float] = Field(default=None, alias="MaxRows", description="The maximum number of rows that can be returned (if applicable).")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
