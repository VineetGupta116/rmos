from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck() -> None:
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_prompt_templates() -> None:
    response = client.get('/api/v1/prompt-engine/templates')
    assert response.status_code == 200
    assert 'research_summary' in response.json()['templates']


def test_skill_learning_flow() -> None:
    create_payload = {'skill_name': 'Python', 'current_level': 'beginner', 'target_weeks': 6}
    create_res = client.post('/api/v1/skills/plan', json=create_payload)
    assert create_res.status_code == 200

    plan_id = create_res.json()['id']
    progress_res = client.post(
        f'/api/v1/skills/plan/{plan_id}/progress',
        json={'completed_milestone': 'Week 1-2: Foundations for Python'},
    )
    assert progress_res.status_code == 200
    assert progress_res.json()['completion_percent'] > 0
