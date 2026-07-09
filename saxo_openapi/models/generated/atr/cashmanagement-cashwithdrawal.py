"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_openapi.models.base import _FlexModel

class SubmitCashWithdrawalRequestRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account identifier in key format from which to transfer money.")
    Amount: Optional[float] = Field(default=None, alias="Amount", description="The amount to be withdrawn.")
    BeneficiaryInstructionId: Optional[str] = Field(default=None, alias="BeneficiaryInstructionId", description="Id of the beneficiary instruction to be used for the withdrawal")
    Currency: Optional[Any] = Field(default=None, alias="Currency", description="The currency the amount is in.")
    MessageToBeneficiary: Optional[str] = Field(default=None, alias="MessageToBeneficiary", description="For MT103 type messages this is a free text field and for MT202 messages it is used to specify additional information to one of the parties involved in the transaction in a structured format. See the Cash Withdrawal learn page for more information about the format for MT202 messages.Maximum length is 140 ASCII characters.")
    PayeeVerificationId: Optional[int] = Field(default=None, alias="PayeeVerificationId", description="The identifier of the verification of payee request.")
    WithdrawalReasonId: Optional[int] = Field(default=None, alias="WithdrawalReasonId", description="This field is mandatory for PEA-PME transactions. Default value for PEA-PME is Standard and for non PEA-PME transaction it is null.")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
