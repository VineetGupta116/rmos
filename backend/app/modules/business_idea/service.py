from app.modules.business_idea.schemas import (
    IdeaEvaluationRequest,
    IdeaEvaluationResponse,
    IdeaRefinementRequest,
    IdeaRefinementResponse,
)


class BusinessIdeaService:
    def evaluate(self, payload: IdeaEvaluationRequest) -> IdeaEvaluationResponse:
        base = 55
        if len(payload.problem) > 100:
            base += 10
        if len(payload.target_audience.split()) > 2:
            base += 5
        if 'ai' in payload.title.lower() or 'automation' in payload.problem.lower():
            base += 8
        score = min(base, 95)

        return IdeaEvaluationResponse(
            score=score,
            strengths=[
                'Clear user pain point articulated',
                'Target audience specified',
                'Potential for iterative MVP rollout',
            ],
            risks=[
                'Competitive market pressure',
                'Customer acquisition cost uncertainty',
                'Execution risk in first 90 days',
            ],
            recommendations=[
                'Run 10 customer discovery interviews',
                'Validate willingness to pay with landing page test',
                'Define one north-star metric for MVP',
            ],
        )

    def refine(self, payload: IdeaRefinementRequest) -> IdeaRefinementResponse:
        value_prop = (
            f"{payload.title} helps users by transforming '{payload.concept[:90]}...' "
            'into a measurable business outcome with faster delivery and lower operational overhead.'
        )
        return IdeaRefinementResponse(
            refined_value_proposition=value_prop,
            monetization_options=['Usage-based subscription', 'Tiered SaaS pricing', 'Enterprise annual contract'],
            mvp_scope=[
                'Core workflow orchestration',
                'Basic analytics dashboard',
                'Admin controls + audit trail',
            ],
        )


business_idea_service = BusinessIdeaService()
