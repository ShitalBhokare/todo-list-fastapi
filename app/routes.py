from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from . import models, schemas

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=schemas.TodoResponse)
def create(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.get("/", response_model=list[schemas.TodoResponse])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()


@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def get_one(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)

    db.commit()
    db.refresh(db_todo)
    return db_todo


@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
