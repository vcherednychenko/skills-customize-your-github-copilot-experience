from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from fastapi.testclient import TestClient

module_path = Path(__file__).with_name("starter-code.py")
spec = spec_from_file_location("starter_code", module_path)
starter_code = module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(starter_code)

TASKS = starter_code.TASKS
app = starter_code.app

client = TestClient(app)


def reset_tasks():
    TASKS[:] = [
        {"id": 1, "title": "Write lesson plan", "status": "todo"},
        {"id": 2, "title": "Grade quizzes", "status": "in_progress"},
    ]


def test_get_tasks_returns_list():
    reset_tasks()
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 2


def test_get_task_by_id_returns_item():
    reset_tasks()
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


# Students should add more tests below for:
# - GET /tasks/{id} when id is missing (expect 404)
# - POST /tasks success and validation failures
# - PUT /tasks/{id} success and missing id
# - PUT /tasks/{id} validation failures
