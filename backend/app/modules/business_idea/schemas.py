from pydantic import BaseModel, Field


class IdeaEvaluationRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=160)
    problem: str = Field(..., min_length=10, max_length=2000)
    target_audience: str = Field(..., min_length=3, max_length=300)


class IdeaEvaluationResponse(BaseModel):
    score: int = Field(..., ge=1, le=100)
    strengths: list[str]
    risks: list[str]
    recommendations: list[str]


class IdeaRefinementRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=160)
    concept: str = Field(..., min_length=10, max_length=2000)


class IdeaRefinementResponse(BaseModel):
    refined_value_proposition: str
    monetization_options: list[str]
    mvp_scope: list[str]
