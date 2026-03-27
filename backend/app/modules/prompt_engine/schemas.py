from pydantic import BaseModel, Field


class PromptRenderRequest(BaseModel):
    template_name: str = Field(..., min_length=2, max_length=80)
    variables: dict[str, str] = Field(default_factory=dict)


class PromptRenderResponse(BaseModel):
    rendered_prompt: str


class TemplateListResponse(BaseModel):
    templates: list[str]
