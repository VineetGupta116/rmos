# RMOS (Streamlit Refactor)

RMOS has been refactored into a **single Streamlit application** with modular Python packages.

## Structure

```text
rmos/
├── app.py
├── modules/
│   ├── skill_learning.py
│   ├── business_idea.py
│   ├── client_delivery.py
│   └── prompt_engine.py
├── prompts/
│   └── templates.py
├── utils/
│   ├── state.py
│   └── validators.py
└── requirements.txt
```

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
