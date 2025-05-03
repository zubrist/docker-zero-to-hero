# 📚 Task Management API: CRUD Operations Guide

This Spring Boot application provides a REST API to manage tasks stored in a MongoDB database. Below is a guide to the available CRUD (Create, Read, Update, Delete) operations and how to execute them.

---

## 🛠️ Prerequisites
1. Ensure the application is running using Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. The application will be accessible at `http://localhost:8080`.

## 🚀 CRUD Operations

### 1. Create a Task
- **Endpoint**: `POST /tasks`
- **Request Body**:
  ```json
  {
    "title": "Task Title",
    "description": "Task Description",
    "dueDate": "2023-12-31T23:59:59"
  }
  ```

- **Command**
  ```bash
  curl -X POST "http://localhost:8080/tasks" \ 
  --header "Content-Type: application/json" \
  --data '{
  "title":"Task Title",
  "description":"Task Description",
  "completed": false"}'

  ```

- **Response**:
  ```json
  {
    "id": "task_id",
    "title": "Task Title",
    "description": "Task Description",
    "completed": false
  }
  ```

### 2. Read All Tasks
- **Endpoint**: `GET /tasks`

- **Command**
  ```bash
  curl -X GET "http://localhost:8080/tasks"
  ```

- **Response**:
  ```json
  [
    {
      "id": "task_id",
      "title": "Task Title",
      "description": "Task Description",
      "completed": false
    },
    {
        "id": "another-task-id",
        "title": "Learn Spring Boot",
        "description": "Build REST APIs",
        "completed": true
    }
  ]
  ```

### 3. Update a Task
- **Endpoint**: `PUT /tasks/{id}`

- **Command**
  ```bash
  curl -X PUT "http://localhost:8080/tasks/{id}" \ 
  --header "Content-Type: application/json" \
  --data '{
  "title":"Updated Task Title",
  "description":"Updated Task Description",
  "completed": true"
  }'

- **Response**
  ```json
  {
    "id": "task_id",
    "title": "Updated Task Title",
    "description": "Updated Task Description",
    "completed": true
  }
  ```


### 4. Delete a Task
- **Endpoint**: `DELETE /tasks/{id}`

- **Command**
  ```bash
  curl -X DELETE "http://localhost:8080/tasks/{id}"
  ```

- **Response**
  ```json
  {
    "message": "Task deleted successfully"
  }
  ```


## Additional Notes
- **MongoDB** : The tasks are stored in a MongoDB database in the tasks collection.
- **Spring Boot** : The application is built using Spring Boot and Spring Data MongoDB.
- **REST API** : The application provides a RESTful API to manage tasks.
- **CURL** : The commands provided use the CURL tool to interact with the API.
- **JSON** : The responses are in JSON format.


