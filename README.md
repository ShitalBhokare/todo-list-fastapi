# Todo List API using FastAPI

This is a simple Todo List backend project made using FastAPI.
I created this project to understand how backend APIs work step by step.

This project is beginner friendly and easy to understand.

---

## What this project does

This project allows a user to:

- Create a todo
- View all todos
- Update a todo
- Delete a todo

All data is stored in memory (Python list), not in a database.

---

## How the project works (Flow)

Very simple flow:

User sends request  
→ FastAPI app starts from `main.py`  
→ Request goes to `routes.py`  
→ Data is checked using `model.py`  
→ Logic runs in `services.py`  
→ Response is formatted using `helpers.py`  
→ Response is sent back to user  

---

## main.py

- This is the starting file of the project
- It creates the FastAPI application
- It connects all todo routes to the app

Without `main.py`, the project will not run.

---

## routes.py

- This file contains all API endpoints
- It handles user requests
- It calls functions from `services.py`

APIs available:
- POST `/todos/` → Create todo
- GET `/todos/` → Get all todos
- PUT `/todos/{id}` → Update todo
- DELETE `/todos/{id}` → Delete todo

---

## model.py

- This file defines the structure of todo data
- It validates input data using Pydantic
- It prevents wrong data from coming to the API

---

## services.py

- This file contains the main logic
- It stores todos in a list
- It handles create, update, delete operations

This file does not care about API or HTTP.

---

## helpers.py

- This file contains helper functions
- It is used to return responses in a common format
- It helps to avoid repeated code

---

## interfaces.py

- This file defines rules for service classes
- It is useful for large projects
- It helps when database or logic changes in future

---

## Why this project is useful

- Easy to understand
- Clean file structure
- Good for beginners
- Helps in interview basics
- Can be extended with database later

---

## End

This project helped me understand FastAPI, API flow, and backend basics.