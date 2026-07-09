"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class GetallfundingInstructioninfoforspecifiedclientRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")

class FundingInstructionPeriodicTransfer(_FlexModel):
    Amount: Optional[float] = Field(default=None, alias="Amount", description="Value of periodic transfer")
    Currency: Optional[str] = Field(default=None, alias="Currency", description="Currency of periodic transfer")
    EndDate: Optional[str] = Field(default=None, alias="EndDate", description="(Optional) EndDate of periodic transfer")
    FromAccount: Optional[str] = Field(default=None, alias="FromAccount", description="Account for periodic transfer sender")
    FromAccountName: Optional[str] = Field(default=None, alias="FromAccountName", description="Name of account for periodic transfer sender")
    FromAccountType: Optional[str] = Field(default=None, alias="FromAccountType", description="Type of account for periodic transfer sender")
    Interval: Optional[str] = Field(default=None, alias="Interval", description="Interval for periodic transfer")
    ReferenceId: Optional[str] = Field(default=None, alias="ReferenceId", description="ReferenceId for periodic transfer")
    StartDate: Optional[str] = Field(default=None, alias="StartDate", description="StartDate of periodic transfer")

class SubAccountAllocation(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Represent sub account info")
    Allocation: Optional[float] = Field(default=None, alias="Allocation", description="Value allocated to sub account")
    AllocationUnit: Optional[str] = Field(default=None, alias="AllocationUnit", description="AllocationUnit")

class FundingInstructionRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="Account Key")
    PeriodicFundingAmount: Optional[float] = Field(default=None, alias="PeriodicFundingAmount", description="Periodic Funding Amount")
    PeriodicTransfers: Optional[List[FundingInstructionPeriodicTransfer]] = Field(default=None, alias="PeriodicTransfers", description="Funding Allocation - Periodic Transfer info")
    SubAccountAllocation: Optional[List[SubAccountAllocation]] = Field(default=None, alias="SubAccountAllocation", description="Sub account allocation details")

class CreateorUpdateexistingfundingInstructionforclientRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="")
    Instructions: Optional[List[FundingInstructionRequest]] = Field(default=None, alias="Instructions", description="Collection of Funding Instruction request type")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
