import streamlit as st

from modules.business_idea import evaluate_business_idea, refine_business_idea
from modules.client_delivery import create_delivery_plan, delivery_checklist
from modules.prompt_engine import PromptRenderingError, list_templates, render_prompt
from modules.skill_learning import completion_percent, create_learning_plan
from utils.state import get_learning_plan, init_state, set_learning_plan
from utils.validators import bounded_int, non_empty


st.set_page_config(page_title='RMOS', page_icon='🧠', layout='wide')
init_state()

st.title('ResearchMaster Operating System (RMOS)')
st.caption('Streamlit-based workspace for Skill Learning, Business Ideas, and Client Delivery.')

skill_tab, ideas_tab, delivery_tab, prompts_tab = st.tabs(
    ['Skill Learning', 'Business Ideas', 'Client Delivery', 'Prompt Engine']
)

with skill_tab:
    st.subheader('Skill Learning Planner')
    with st.form('skill_learning_form'):
        skill_name = st.text_input('Skill name', value='Product Management')
        current_level = st.selectbox('Current level', ['beginner', 'intermediate', 'advanced'])
        target_weeks = st.number_input('Target weeks', min_value=1, max_value=52, value=8)
        submitted = st.form_submit_button('Create learning plan')

    if submitted:
        try:
            non_empty(skill_name, 'Skill name')
            bounded_int(int(target_weeks), 'Target weeks', 1, 52)
            plan = create_learning_plan(skill_name, current_level, int(target_weeks))
            set_learning_plan(plan)
            st.success('Learning plan created.')
        except ValueError as exc:
            st.error(str(exc))

    plan = get_learning_plan()
    if plan:
        st.markdown(f"**Plan ID:** `{plan.id}`")
        for milestone in plan.milestones:
            checked = milestone in st.session_state.completed_milestones
            if st.checkbox(milestone, value=checked, key=f'ms_{plan.id}_{milestone}') and not checked:
                st.session_state.completed_milestones.append(milestone)

        st.progress(completion_percent(plan, st.session_state.completed_milestones) / 100)
        st.write(f"Completion: **{completion_percent(plan, st.session_state.completed_milestones)}%**")

with ideas_tab:
    st.subheader('Business Idea Evaluator')
    title = st.text_input('Idea title', value='RMOS Insight Copilot', key='idea_title')
    problem = st.text_area(
        'Problem statement',
        value='Founders struggle to convert research notes into structured, actionable launch plans quickly.',
    )
    target_audience = st.text_input('Target audience', value='Early-stage founders and product teams')

    col_a, col_b = st.columns(2)
    if col_a.button('Evaluate idea'):
        try:
            non_empty(title, 'Idea title')
            non_empty(problem, 'Problem statement')
            non_empty(target_audience, 'Target audience')
            result = evaluate_business_idea(title, problem, target_audience)
            st.metric('Idea score', f'{result.score}/100')
            st.write('**Strengths**')
            st.write('\n'.join(f'- {x}' for x in result.strengths))
            st.write('**Risks**')
            st.write('\n'.join(f'- {x}' for x in result.risks))
            st.write('**Recommendations**')
            st.write('\n'.join(f'- {x}' for x in result.recommendations))
        except ValueError as exc:
            st.error(str(exc))

    if col_b.button('Refine value proposition'):
        value_prop, monetization, mvp_scope = refine_business_idea(title, problem)
        st.write('**Refined value proposition**')
        st.info(value_prop)
        st.write('**Monetization options**')
        st.write('\n'.join(f'- {x}' for x in monetization))
        st.write('**MVP scope**')
        st.write('\n'.join(f'- {x}' for x in mvp_scope))

with delivery_tab:
    st.subheader('Client Delivery Planner')
    project_name = st.text_input('Project name', value='RMOS Enterprise Rollout', key='delivery_project_name')
    timeline_weeks = st.number_input('Timeline (weeks)', min_value=1, max_value=52, value=10)
    include_handover = st.checkbox('Include handover checklist', value=True)

    if st.button('Generate delivery plan'):
        try:
            non_empty(project_name, 'Project name')
            bounded_int(int(timeline_weeks), 'Timeline weeks', 1, 52)
            plan = create_delivery_plan(project_name, int(timeline_weeks))
            checklist = delivery_checklist(include_handover=include_handover)
            st.write('**Phases**')
            st.write('\n'.join(f'1. {phase}' for phase in plan.phases))
            st.write('**Delivery risks**')
            st.write('\n'.join(f'- {risk}' for risk in plan.risks))
            st.write(f"**Communication cadence:** {plan.communication_cadence}")
            st.write('**Checklist**')
            st.write('\n'.join(f'- {item}' for item in checklist))
        except ValueError as exc:
            st.error(str(exc))

with prompts_tab:
    st.subheader('Prompt Engine')
    template_name = st.selectbox('Template', list_templates())
    vars_text = st.text_area(
        'Variables (key=value per line)',
        value='topic=AI agent workflows\naudience=Founders',
        height=120,
    )

    if st.button('Render prompt'):
        variables: dict[str, str] = {}
        for line in vars_text.splitlines():
            if '=' in line:
                key, value = line.split('=', 1)
                variables[key.strip()] = value.strip()

        try:
            rendered = render_prompt(template_name, variables)
            st.code(rendered)
        except PromptRenderingError as exc:
            st.error(str(exc))
