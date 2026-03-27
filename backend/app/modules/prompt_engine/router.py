from fastapi import APIRouter, HTTPException

from app.modules.prompt_engine.schemas import PromptRenderRequest, PromptRenderResponse, TemplateListResponse
from app.modules.prompt_engine.service import prompt_engine_service

router = APIRouter(prefix='/prompt-engine', tags=['prompt-engine'])


@router.get('/templates', response_model=TemplateListResponse)
def list_templates() -> TemplateListResponse:
    return prompt_engine_service.list_templates()


@router.post('/render', response_model=PromptRenderResponse)
def render_prompt(payload: PromptRenderRequest) -> PromptRenderResponse:
    rendered = prompt_engine_service.render(payload)
    if not rendered:
        raise HTTPException(status_code=404, detail='Template not found')
    return rendered
