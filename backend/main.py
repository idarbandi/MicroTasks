from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database


app = FastAPI()


from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)


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
    return 1


@app.get("/api/todo{id}")
async def get_todo_by_id(id):
    return 1


@app.post("/api/todo/")
async def post_todo():
    return 1


@app.put("/api/todo{id}")
async def put_todo(id):
    return 1


@app.delete("/api/todo{id}")
async def delete_todo(id):
    return 1