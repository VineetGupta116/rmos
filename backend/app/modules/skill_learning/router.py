from fastapi import APIRouter, HTTPException

from app.modules.skill_learning.schemas import (
    LearningPlan,
    LearningPlanRequest,
    LearningProgress,
    UpdateProgressRequest,
)
from app.modules.skill_learning.service import skill_learning_service

router = APIRouter(prefix='/skills', tags=['skill-learning'])


@router.post('/plan', response_model=LearningPlan)
def create_learning_plan(payload: LearningPlanRequest) -> LearningPlan:
    return skill_learning_service.create_plan(payload)


@router.get('/plan/{plan_id}', response_model=LearningPlan)
def get_learning_plan(plan_id: str) -> LearningPlan:
    plan = skill_learning_service.get_plan(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail='Learning plan not found')
    return plan


@router.post('/plan/{plan_id}/progress', response_model=LearningProgress)
def update_learning_progress(plan_id: str, payload: UpdateProgressRequest) -> LearningProgress:
    progress = skill_learning_service.record_progress(plan_id, payload.completed_milestone)
    if not progress:
        raise HTTPException(status_code=404, detail='Learning plan not found')
    return progress
