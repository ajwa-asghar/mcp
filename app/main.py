# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    title: str
    description: str

todos = []

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created", "todo": todo}

@app.get("/todos")
def list_todos():
    return {"todos": todos}
