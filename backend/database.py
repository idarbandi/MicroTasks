from model import Todo
from motor import motor_asynci
from database import collection

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")

database = client.TodoList
collection = database.todo


await def fetch_one_todo(title):
    document = await.collection.find_one({'title': title})
    

await def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for doc in cursor:
        todos.append(Todo(**doc))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return result

async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {
        'description': desc
    }})
    document = await collection.find_one({'title': title})
    return document

async def remove_todo(title):
    await collection.delete_one({'title': title})
    return True