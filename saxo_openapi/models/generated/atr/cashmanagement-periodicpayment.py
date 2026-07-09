"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class FetchesalltheScheduledPeriodicPaymentsRequest(_FlexModel):
    ClientKey: Optional[Any] = Field(default=None, alias="ClientKey", description="Client Id")
    SkipToken: Optional[str] = Field(default=None, alias="SkipToken", description="Id token of entity to start taking elements from.")
    Top: Optional[int] = Field(default=None, alias="Top", description="Number of elements to retrieve.")

class PeriodicScheduleTypes(_FlexModel):
    Daily: Optional[Any] = Field(default=None, alias="Daily", description="")
    HalfYearly: Optional[Any] = Field(default=None, alias="HalfYearly", description="")
    Monthly: Optional[Any] = Field(default=None, alias="Monthly", description="")
    None_: Optional[Any] = Field(default=None, alias="None", description="")
    Quarterly: Optional[Any] = Field(default=None, alias="Quarterly", description="")
    Weekly: Optional[Any] = Field(default=None, alias="Weekly", description="")
    Yearly: Optional[Any] = Field(default=None, alias="Yearly", description="")

class CreateanewperiodicspaymentscheduleRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account identifier in key format from which to transfer money.")
    Amount: Optional[float] = Field(default=None, alias="Amount", description="The amount to be withdrawn.")
    BeneficiaryInstructionId: Optional[str] = Field(default=None, alias="BeneficiaryInstructionId", description="Id of the beneficiary instruction to be used for the withdrawal")
    Currency: Optional[Any] = Field(default=None, alias="Currency", description="The currency of amount.")
    EndByDate: Optional[str] = Field(default=None, alias="EndByDate", description="Determines when the recurring payments would be stopped, when left blank, the recurring payment would be marked never ending.")
    MessageToBeneficiary: Optional[str] = Field(default=None, alias="MessageToBeneficiary", description="For MT103 type messages this is a free text field information to one of the parties involved in the transaction in a structured format.")
    PayeeVerificationId: Optional[int] = Field(default=None, alias="PayeeVerificationId", description="The identifier of the verification of payee request.")
    RecurrenceType: Optional[PeriodicScheduleTypes] = Field(default=None, alias="RecurrenceType", description="Specifies the frequency of recurring payment.")
    StartDate: Optional[str] = Field(default=None, alias="StartDate", description="Specifies when the actual payment should be started. It also detemines which day would be used for different frequencies i.e. Daily, Weekly etc.")

class UpdateanexistingperiodicpaymentscheduleRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account identifier in key format from which to transfer money.")
    Amount: Optional[float] = Field(default=None, alias="Amount", description="The amount to be withdrawn.")
    BeneficiaryInstructionId: Optional[str] = Field(default=None, alias="BeneficiaryInstructionId", description="Id of the beneficiary instruction to be used for the withdrawal")
    Currency: Optional[Any] = Field(default=None, alias="Currency", description="The currency of amount.")
    EndByDate: Optional[str] = Field(default=None, alias="EndByDate", description="Determines when the recurring payments would be stopped, when left blank, the recurring payment would be marked never ending.")
    MessageToBeneficiary: Optional[str] = Field(default=None, alias="MessageToBeneficiary", description="For MT103 type messages this is a free text field information to one of the parties involved in the transaction in a structured format.")
    PayeeVerificationId: Optional[int] = Field(default=None, alias="PayeeVerificationId", description="The identifier of the verification of payee request.")
    PeriodicPaymentId: Optional[int] = Field(default=None, alias="PeriodicPaymentId", description="")
    RecurrenceType: Optional[PeriodicScheduleTypes] = Field(default=None, alias="RecurrenceType", description="Specifies the frequency of recurring payment.")
    StartDate: Optional[str] = Field(default=None, alias="StartDate", description="Specifies when the actual payment should be started. It also detemines which day would be used for different frequencies i.e. Daily, Weekly etc.")

class DeactivatestheperiodicpaymentRequest(_FlexModel):
    PeriodicPaymentId: Optional[int] = Field(default=None, alias="PeriodicPaymentId", description="PeriodicPaymentId to be terminated.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
