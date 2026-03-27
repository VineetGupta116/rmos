from fastapi import APIRouter

from app.modules.client_delivery.schemas import (
    DeliveryChecklistRequest,
    DeliveryChecklistResponse,
    DeliveryPlanRequest,
    DeliveryPlanResponse,
)
from app.modules.client_delivery.service import client_delivery_service

router = APIRouter(prefix='/client-delivery', tags=['client-delivery'])


@router.post('/plan', response_model=DeliveryPlanResponse)
def create_delivery_plan(payload: DeliveryPlanRequest) -> DeliveryPlanResponse:
    return client_delivery_service.build_plan(payload)


@router.post('/checklist', response_model=DeliveryChecklistResponse)
def generate_delivery_checklist(payload: DeliveryChecklistRequest) -> DeliveryChecklistResponse:
    return client_delivery_service.checklist(payload)
