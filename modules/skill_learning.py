from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class LearningPlan:
    id: str
    skill_name: str
    current_level: str
    target_weeks: int
    milestones: list[str]
    created_at: datetime


def build_milestones(skill_name: str, target_weeks: int) -> list[str]:
    phases: list[tuple[int, int, str]] = []

    foundation_end = min(2, target_weeks)
    phases.append((1, foundation_end, f'Foundations for {skill_name}'))

    if target_weeks >= 3:
        guided_end = min(4, target_weeks)
        phases.append((3, guided_end, f'Guided projects in {skill_name}'))

    if target_weeks >= 5:
        simulation_end = min(6, target_weeks)
        phases.append((5, simulation_end, f'Real-world simulation for {skill_name}'))

    last_end = phases[-1][1]
    if last_end < target_weeks:
        phases.append((last_end + 1, target_weeks, 'Portfolio + interview readiness'))
    elif target_weeks == 1:
        phases.append((1, 1, 'Portfolio + interview readiness'))

    return [f'Week {start}-{end}: {title}' for start, end, title in phases]


def create_learning_plan(skill_name: str, current_level: str, target_weeks: int) -> LearningPlan:
    return LearningPlan(
        id=uuid4().hex,
        skill_name=skill_name,
        current_level=current_level,
        target_weeks=target_weeks,
        milestones=build_milestones(skill_name, target_weeks),
        created_at=datetime.now(timezone.utc),
    )


def completion_percent(plan: LearningPlan, completed: list[str]) -> float:
    return round((len(completed) / max(len(plan.milestones), 1)) * 100, 2)
