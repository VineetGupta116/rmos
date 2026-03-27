from datetime import UTC, datetime

from app.modules.skill_learning.schemas import LearningPlan, LearningPlanRequest, LearningProgress
from app.services.id_generator import new_id


class SkillLearningService:
    def __init__(self) -> None:
        self._plans: dict[str, LearningPlan] = {}
        self._completed: dict[str, list[str]] = {}

    def create_plan(self, payload: LearningPlanRequest) -> LearningPlan:
        plan_id = new_id()

        milestones = [
            f'Week 1-2: Foundations for {payload.skill_name}',
            f'Week 3-4: Guided projects in {payload.skill_name}',
            f'Week 5-6: Real-world simulation for {payload.skill_name}',
            f'Week 7-{payload.target_weeks}: Portfolio + interview readiness',
        ]

        plan = LearningPlan(
            id=plan_id,
            skill_name=payload.skill_name,
            current_level=payload.current_level,
            target_weeks=payload.target_weeks,
            milestones=milestones,
            created_at=datetime.now(UTC),
        )

        self._plans[plan_id] = plan
        self._completed[plan_id] = []
        return plan

    def get_plan(self, plan_id: str) -> LearningPlan | None:
        return self._plans.get(plan_id)

    def record_progress(self, plan_id: str, milestone: str) -> LearningProgress | None:
        plan = self.get_plan(plan_id)
        if not plan:
            return None

        completed = self._completed.setdefault(plan_id, [])
        if milestone not in completed:
            completed.append(milestone)

        completion = round((len(completed) / max(len(plan.milestones), 1)) * 100, 2)
        return LearningProgress(plan_id=plan_id, completed=completed, completion_percent=completion)


skill_learning_service = SkillLearningService()
