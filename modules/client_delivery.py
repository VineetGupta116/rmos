from dataclasses import dataclass


@dataclass
class DeliveryPlan:
    project_name: str
    phases: list[str]
    risks: list[str]
    communication_cadence: str


def create_delivery_plan(project_name: str, timeline_weeks: int) -> DeliveryPlan:
    phases = [
        f'Week 1: Discovery & acceptance criteria for {project_name}',
        f'Week 2-{max(2, timeline_weeks // 2)}: Build & iteration',
        f'Week {max(3, timeline_weeks - 1)}: UAT + feedback closure',
        f'Week {timeline_weeks}: Launch + post-launch support',
    ]

    return DeliveryPlan(
        project_name=project_name,
        phases=phases,
        risks=['Scope creep', 'Dependency bottlenecks', 'Stakeholder sign-off delays'],
        communication_cadence='Twice-weekly status updates + weekly stakeholder demo',
    )


def delivery_checklist(include_handover: bool = True) -> list[str]:
    items = [
        'Signed statement of work',
        'Defined milestones and owners',
        'QA test report approved',
        'Production deployment checklist complete',
    ]
    if include_handover:
        items.extend(['Runbook delivered', 'Knowledge transfer session completed'])
    return items
