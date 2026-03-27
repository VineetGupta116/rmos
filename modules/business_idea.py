from dataclasses import dataclass


@dataclass
class IdeaEvaluation:
    score: int
    strengths: list[str]
    risks: list[str]
    recommendations: list[str]


def evaluate_business_idea(title: str, problem: str, target_audience: str) -> IdeaEvaluation:
    base = 55
    if len(problem) > 100:
        base += 10
    if len(target_audience.split()) > 2:
        base += 5
    if 'ai' in title.lower() or 'automation' in problem.lower():
        base += 8

    score = min(base, 95)

    return IdeaEvaluation(
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
            'Validate willingness to pay with a landing page experiment',
            'Define one north-star metric for MVP',
        ],
    )


def refine_business_idea(title: str, concept: str) -> tuple[str, list[str], list[str]]:
    value_prop = (
        f"{title} helps users by transforming '{concept[:90]}...' "
        'into measurable outcomes with faster delivery and lower operational overhead.'
    )
    monetization = ['Usage-based subscription', 'Tiered SaaS pricing', 'Enterprise annual contract']
    mvp_scope = ['Core workflow orchestration', 'Basic analytics dashboard', 'Admin controls + audit trail']
    return value_prop, monetization, mvp_scope
