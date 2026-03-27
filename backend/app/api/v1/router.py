from fastapi import APIRouter

from app.modules.business_idea.router import router as business_idea_router
from app.modules.client_delivery.router import router as client_delivery_router
from app.modules.prompt_engine.router import router as prompt_engine_router
from app.modules.skill_learning.router import router as skill_learning_router

router = APIRouter(prefix='/api/v1')

router.include_router(skill_learning_router)
router.include_router(business_idea_router)
router.include_router(client_delivery_router)
router.include_router(prompt_engine_router)
