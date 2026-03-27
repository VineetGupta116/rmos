from string import Formatter

from prompts.templates import TEMPLATES


class PromptRenderingError(ValueError):
    """Raised when a template cannot be rendered."""


def list_templates() -> list[str]:
    return sorted(TEMPLATES.keys())


def render_prompt(template_name: str, variables: dict[str, str]) -> str:
    template = TEMPLATES.get(template_name)
    if not template:
        raise PromptRenderingError('Template not found')

    required_keys = {
        field_name
        for _, field_name, _, _ in Formatter().parse(template)
        if field_name is not None and field_name != ''
    }
    missing = sorted(required_keys - set(variables.keys()))
    if missing:
        raise PromptRenderingError(f'Missing template variables: {", ".join(missing)}')

    try:
        return template.format_map(variables)
    except (KeyError, ValueError) as exc:
        raise PromptRenderingError(str(exc)) from exc
