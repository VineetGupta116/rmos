TEMPLATES: dict[str, str] = {
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
