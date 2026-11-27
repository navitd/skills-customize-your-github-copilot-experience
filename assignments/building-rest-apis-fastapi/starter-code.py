from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: int = 0
    title: str
    completed: bool = False


tasks: list[Task] = [
    Task(id=1, title="Learn FastAPI", completed=False),
]


@app.get("/tasks")
def get_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Find and return the task.
    # TODO: Raise HTTPException with status_code=404 if it is missing.
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    # TODO: Add the task to the list and return it.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    # TODO: Find the task and replace it.
    # TODO: Raise HTTPException with status_code=404 if it is missing.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Find and remove the task.
    # TODO: Return the removed task.
    pass
