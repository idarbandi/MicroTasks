from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
import database


app = FastAPI()


from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)
from models import Todo


origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def pong():
    return {"ping": "pong"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo{id}", response_model=Todo)
async def get_todo_by_id(title):
    response = fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, "Todo list With The Given Title Was Not Found")


@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "something went wrong / Bad Request")


@app.put("/api/todo{id}", response_model=Todo)
async def put_todo(id: str, desc: str):
    response = await update_todo(id, desc)
    if response:
        return response
    raise HTTPException(404, f"Theres No Title With The Givven Title {id}")


@app.delete("/api/todo{id}")
async def delete_todo(id):
    response = await remove_todo(title)
    if response:
        return "Successfully Deleted Item"
    raise HTTPException(404, f"Theres No Title With The Givven Title {id}")
