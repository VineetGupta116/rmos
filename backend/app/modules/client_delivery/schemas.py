from pydantic import BaseModel, Field


class DeliveryPlanRequest(BaseModel):
    project_name: str = Field(..., min_length=2, max_length=150)
    scope: str = Field(..., min_length=10, max_length=2500)
    timeline_weeks: int = Field(default=6, ge=1, le=52)


class DeliveryPlanResponse(BaseModel):
    project_name: str
    phases: list[str]
    risks: list[str]
    communication_cadence: str


class DeliveryChecklistRequest(BaseModel):
    project_name: str = Field(..., min_length=2, max_length=150)
    include_handover: bool = True


class DeliveryChecklistResponse(BaseModel):
    items: list[str]
