from app.modules.client_delivery.schemas import (
    DeliveryChecklistRequest,
    DeliveryChecklistResponse,
    DeliveryPlanRequest,
    DeliveryPlanResponse,
)


class ClientDeliveryService:
    def build_plan(self, payload: DeliveryPlanRequest) -> DeliveryPlanResponse:
        phases = [
            f'Week 1: Discovery & acceptance criteria for {payload.project_name}',
            f'Week 2-{max(2, payload.timeline_weeks // 2)}: Build & iteration',
            f'Week {max(3, payload.timeline_weeks - 1)}: UAT + feedback closure',
            f'Week {payload.timeline_weeks}: Launch + post-launch support',
        ]

        return DeliveryPlanResponse(
            project_name=payload.project_name,
            phases=phases,
            risks=['Scope creep', 'Dependency bottlenecks', 'Stakeholder sign-off delays'],
            communication_cadence='Twice-weekly status updates + weekly stakeholder demo',
        )

    def checklist(self, payload: DeliveryChecklistRequest) -> DeliveryChecklistResponse:
        items = [
            'Signed statement of work',
            'Defined milestones and owners',
            'QA test report approved',
            'Production deployment checklist complete',
        ]
        if payload.include_handover:
            items.extend(['Runbook delivered', 'Knowledge transfer session completed'])
        return DeliveryChecklistResponse(items=items)


client_delivery_service = ClientDeliveryService()
