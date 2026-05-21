# 📘 Assignment: API Testing and Reliability with Pytest

## 🎯 Objective

Students will design and run tests for a FastAPI service using Pytest, then improve endpoint behavior by handling edge cases and invalid input.

## 📝 Tasks

### 🛠️ Write Tests for Core API Behavior

#### Description
Use Pytest and FastAPI TestClient to test the provided API. Start with success-path checks and then add failure-path checks for missing records and invalid request data.

#### Requirements
Completed program should:

- Create test cases in `test_api.py` for `GET /tasks`, `GET /tasks/{task_id}`, and `POST /tasks`
- Verify response status codes and key JSON fields for each endpoint
- Include at least one test that proves the API returns a 404 for a missing task


### 🛠️ Improve Reliability with Edge-Case Tests

#### Description
Expand your test suite to cover updates and input validation. Use failing tests to identify reliability issues, then update the API logic so all tests pass.

#### Requirements
Completed program should:

- Add tests for `PUT /tasks/{task_id}` including success and missing-task scenarios
- Add tests that reject invalid input such as empty titles or unsupported status values
- Update `starter-code.py` as needed so your full Pytest suite passes
