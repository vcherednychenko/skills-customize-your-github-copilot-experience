from enum import Enum
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    status: TaskStatus = TaskStatus.todo


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    status: Optional[TaskStatus] = None


# In-memory store for assignment practice.
TASKS = [
    {"id": 1, "title": "Write lesson plan", "status": "todo"},
    {"id": 2, "title": "Grade quizzes", "status": "in_progress"},
]


@app.get("/tasks")
def list_tasks():
    return TASKS


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in TASKS:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    next_id = max((t["id"] for t in TASKS), default=0) + 1
    new_task = {"id": next_id, "title": task.title, "status": task.status.value}
    TASKS.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in TASKS:
        if task["id"] == task_id:
            if task_update.title is not None:
                task["title"] = task_update.title
            if task_update.status is not None:
                task["status"] = task_update.status.value
            return task
    raise HTTPException(status_code=404, detail="Task not found")
