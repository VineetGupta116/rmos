import streamlit as st

from modules.skill_learning import LearningPlan


def init_state() -> None:
    if 'learning_plan' not in st.session_state:
        st.session_state.learning_plan = None
    if 'completed_milestones' not in st.session_state:
        st.session_state.completed_milestones = []


def set_learning_plan(plan: LearningPlan) -> None:
    st.session_state.learning_plan = plan
    st.session_state.completed_milestones = []


def get_learning_plan() -> LearningPlan | None:
    return st.session_state.learning_plan
