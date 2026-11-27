# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test a REST API with FastAPI by creating endpoints for managing a collection of programming tasks.

## 📝 Tasks

### 🛠️ Create and Read Task Resources

#### Description
Set up a FastAPI application and define endpoints that list all tasks and retrieve one task by ID.

#### Requirements
Completed program should:

- Create a FastAPI application named `app`
- Store tasks in an in-memory list
- Return a list of tasks from `GET /tasks`
- Return one task from `GET /tasks/{task_id}`
- Return a 404 response when a requested task ID does not exist


### 🛠️ Add Validated Task Creation

#### Description
Add a Pydantic model and endpoint for creating new tasks.

#### Requirements
Completed program should:

- Define a `Task` Pydantic model with a string `title`, boolean `completed`, and integer `id`
- Accept task data in `POST /tasks`
- Assign or generate an ID for each new task
- Return the created task with a 201 status code
- Return validation errors for missing or incorrectly typed required fields


### 🛠️ Update and Delete Tasks

#### Description
Complete the task API by supporting updates and deletion.

#### Requirements
Completed program should:

- Update an existing task with `PUT /tasks/{task_id}`
- Remove an existing task with `DELETE /tasks/{task_id}`
- Return the updated task or deleted task data
- Return a 404 response for update or delete requests when the task ID does not exist
