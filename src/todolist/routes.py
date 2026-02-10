from fastapi import APIRouter
from src.todolist.helpers import success_response
from .model import TodoCreate, TodoResponse
from .services import TodoService
from fastapi import HTTPException
from fastapi import status
router = APIRouter()
service = TodoService()

@router.post("/", response_model=TodoResponse)
def create(todo: TodoCreate):
    return service.create_todo(todo)

@router.get("/")
def get_all():
    todos= service.get_todos()
    return success_response(todos, "Todos fetched successfully")

from fastapi import HTTPException

@router.put("/{todo_id}")
def update(todo_id: int, todo: TodoCreate):
    updated = service.update_todo(todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/{todo_id}")
def delete(todo_id: int):
    deleted = service.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
