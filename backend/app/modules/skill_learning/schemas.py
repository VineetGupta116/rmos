from datetime import datetime

from pydantic import BaseModel, Field


class LearningPlanRequest(BaseModel):
    skill_name: str = Field(..., min_length=2, max_length=120)
    current_level: str = Field(default='beginner', pattern='^(beginner|intermediate|advanced)$')
    target_weeks: int = Field(default=8, ge=1, le=52)


class LearningPlan(BaseModel):
    id: str
    skill_name: str
    current_level: str
    target_weeks: int
    milestones: list[str]
    created_at: datetime


class UpdateProgressRequest(BaseModel):
    completed_milestone: str = Field(..., min_length=2, max_length=200)


class LearningProgress(BaseModel):
    plan_id: str
    completed: list[str]
    completion_percent: float
