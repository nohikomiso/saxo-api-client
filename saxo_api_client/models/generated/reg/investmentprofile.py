"""
Auto-generated Pydantic Models for SaxoBank OpenAPI
"""
from __future__ import annotations
from typing import List, Optional, Any
from pydantic import Field
from saxo_api_client.models.base import _FlexModel

class EntityType(_FlexModel):
    Individual: Optional[Any] = Field(default=None, alias="Individual", description="An Individual person")
    Organisation: Optional[Any] = Field(default=None, alias="Organisation", description="A corporation")

class GettheaccountinvestmentprofileRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account for which the settings apply")
    EntityKey: Optional[str] = Field(default=None, alias="EntityKey", description="UserKey if EntityType=Individual or ClientKey if EntityType=Organisation")
    EntityType: Optional[EntityType] = Field(default=None, alias="EntityType", description="An individual person or organisation")

class EsgPreference(_FlexModel):
    General: Optional[Any] = Field(default=None, alias="General", description="Client has general ESG preferences")
    None_: Optional[Any] = Field(default=None, alias="None", description="ESG preference not specified")
    Specific: Optional[Any] = Field(default=None, alias="Specific", description="Client has specific ESG preferences, which are captured separately as impact, taxonomy and PAI percentages")

class SpecificEsgPreference(_FlexModel):
    ImpactInvestingPct: Optional[float] = Field(default=None, alias="ImpactInvestingPct", description="How much of the chosen investment should be invested in instruments with a certain share of impact investments.")
    PrincipalAdverseImpactPct: Optional[float] = Field(default=None, alias="PrincipalAdverseImpactPct", description="How much percentage client wants to avoid investing in companies with poor ESG practices, which can have a negative impact on the environment, surrounding communities, and other factors. Principal Adverse Impact (PAI) indicators are a way to measure ESG factors.")
    TaxonomyPct: Optional[float] = Field(default=None, alias="TaxonomyPct", description="The minimum percentage of the investment that should be invested in companies that are involved in sustainable economic activities according to the EU taxonomy.")

class EsgDeclaration(_FlexModel):
    EsgPreference: Optional[EsgPreference] = Field(default=None, alias="EsgPreference", description="Esg preference")
    SpecificEsgPreference: Optional[SpecificEsgPreference] = Field(default=None, alias="SpecificEsgPreference", description="Specific Esg preference")

class ManagementType(_FlexModel):
    Advisory: Optional[Any] = Field(default=None, alias="Advisory", description="Advisory")
    Discretionary: Optional[Any] = Field(default=None, alias="Discretionary", description="Discretionary")
    None_: Optional[Any] = Field(default=None, alias="None", description="None")
    TradeAdvisory: Optional[Any] = Field(default=None, alias="TradeAdvisory", description="TradeAdvisory")

class UpdatetimeandhorizonforthespecifiedaccountoptionallyoverridetheotherinvestmentprofilepropertiesRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account for which the settings apply")
    EsgDeclaration: Optional[EsgDeclaration] = Field(default=None, alias="EsgDeclaration", description="ESG declaration")
    Horizon: Optional[int] = Field(default=None, alias="Horizon", description="Year at which the investment is expected to be liquidated")
    PreferredManagementType: Optional[ManagementType] = Field(default=None, alias="PreferredManagementType", description="Preferred account management type")
    Purpose: Optional[str] = Field(default=None, alias="Purpose", description="Textual description of investment purpose.")
    RiskAppetiteId: Optional[str] = Field(default=None, alias="RiskAppetiteId", description="Id of RiskAppetite for the entity")

class PatchtimeandhorizonforthespecifiedaccountoptionallyoverridetheotherinvestmentprofilepropertiesRequest(_FlexModel):
    AccountKey: Optional[Any] = Field(default=None, alias="AccountKey", description="The account for which the settings apply")
    EsgDeclaration: Optional[EsgDeclaration] = Field(default=None, alias="EsgDeclaration", description="ESG declaration")
    Horizon: Optional[int] = Field(default=None, alias="Horizon", description="Year at which the investment is expected to be liquidated")
    PreferredManagementType: Optional[ManagementType] = Field(default=None, alias="PreferredManagementType", description="Preferred account management type")
    Purpose: Optional[str] = Field(default=None, alias="Purpose", description="Textual description of investment purpose.")
    RiskAppetiteId: Optional[str] = Field(default=None, alias="RiskAppetiteId", description="Id of RiskAppetite for the entity")

class GetthemostrecentcommoninvestmentprofileforthespecifiedindividualororganisationRequest(_FlexModel):
    EntityKey: Optional[str] = Field(default=None, alias="EntityKey", description="UserKey if EntityType=Individual or ClientKey if EntityType=Organisation")
    EntityType: Optional[EntityType] = Field(default=None, alias="EntityType", description="An individual person or organisation")

class UpdatethecommoninvestmentprofileforthespecifiedindividualororganisationRequest(_FlexModel):
    EntityKey: Optional[str] = Field(default=None, alias="EntityKey", description="UserKey if EntityType=Individual or ClientKey if EntityType=Organisation")
    EntityType: Optional[EntityType] = Field(default=None, alias="EntityType", description="An individual person or organisation")
    EsgDeclaration: Optional[EsgDeclaration] = Field(default=None, alias="EsgDeclaration", description="ESG declaration")
    PreferredManagementType: Optional[ManagementType] = Field(default=None, alias="PreferredManagementType", description="Preferred account management type")
    RiskAppetiteId: Optional[str] = Field(default=None, alias="RiskAppetiteId", description="Id of RiskAppetite for the entity")

class PatchthecommoninvestmentprofileforthespecifiedindividualororganisationRequest(_FlexModel):
    EntityKey: Optional[str] = Field(default=None, alias="EntityKey", description="UserKey if EntityType=Individual or ClientKey if EntityType=Organisation")
    EntityType: Optional[EntityType] = Field(default=None, alias="EntityType", description="An individual person or organisation")
    EsgDeclaration: Optional[EsgDeclaration] = Field(default=None, alias="EsgDeclaration", description="ESG declaration")
    PreferredManagementType: Optional[ManagementType] = Field(default=None, alias="PreferredManagementType", description="Preferred account management type")
    RiskAppetiteId: Optional[str] = Field(default=None, alias="RiskAppetiteId", description="Id of RiskAppetite for the entity")


# Rebuild all Pydantic models to resolve forward references
for _cls in list(globals().values()):
    if isinstance(_cls, type) and issubclass(_cls, _FlexModel) and _cls is not _FlexModel:
        _cls.model_rebuild()
