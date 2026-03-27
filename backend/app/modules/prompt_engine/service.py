from app.modules.prompt_engine.schemas import PromptRenderRequest, PromptRenderResponse, TemplateListResponse


class PromptEngineService:
    def __init__(self) -> None:
        self._templates: dict[str, str] = {
            'research_summary': (
                'You are an RMOS research analyst. Summarize findings for topic: {topic}. '
                'Audience: {audience}. Include key insights, risks, and next actions.'
            ),
            'business_pitch': (
                'Craft a concise pitch for {product} solving {problem} for {market}. '
                'Include value proposition, differentiation, and call-to-action.'
            ),
            'client_update': (
                'Write a client update for project {project_name}. Current status: {status}. '
                'Include completed work, blockers, and next milestones.'
            ),
        }

    def list_templates(self) -> TemplateListResponse:
        return TemplateListResponse(templates=sorted(self._templates.keys()))

    def render(self, payload: PromptRenderRequest) -> PromptRenderResponse | None:
        template = self._templates.get(payload.template_name)
        if not template:
            return None

        rendered = template
        for key, value in payload.variables.items():
            rendered = rendered.replace(f'{{{key}}}', value)
        return PromptRenderResponse(rendered_prompt=rendered)


prompt_engine_service = PromptEngineService()
