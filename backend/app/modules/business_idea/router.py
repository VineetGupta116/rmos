from fastapi import APIRouter

from app.modules.business_idea.schemas import (
    IdeaEvaluationRequest,
    IdeaEvaluationResponse,
    IdeaRefinementRequest,
    IdeaRefinementResponse,
)
from app.modules.business_idea.service import business_idea_service

router = APIRouter(prefix='/business-ideas', tags=['business-idea'])


@router.post('/evaluate', response_model=IdeaEvaluationResponse)
def evaluate_idea(payload: IdeaEvaluationRequest) -> IdeaEvaluationResponse:
    return business_idea_service.evaluate(payload)


@router.post('/refine', response_model=IdeaRefinementResponse)
def refine_idea(payload: IdeaRefinementRequest) -> IdeaRefinementResponse:
    return business_idea_service.refine(payload)
