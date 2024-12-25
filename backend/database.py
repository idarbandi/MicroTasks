"""
*********************************************************************
*                                                                   *
*                         🗒️ MicroTasks                             *
*                                                                   *
*        یک برنامه لیست کارهای ساده و موثر که با فست‌API و           *
*            جاوااسکریپت خالص ساخته شده است 📋🚀                    *
*                                                                   *
*     تولید کننده: idarbandi                                        *
*     ایمیل: darbandidr99@gmail.com                                 *
*     گیت‌هاب: https://github.com/idarbandi                         *
*                                                                   *
*********************************************************************
"""

# ایمپورت مدل Todo از فایل مدل‌ها
# درایور MongoDB
import motor.motor_asyncio
from models import Todo

# اتصال به پایگاه داده MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

# ایجاد پایگاه داده
database = client.TodoList
collection = database.todo


async def get_todo_by_title(title: str):
    """
    دریافت یک وظیفه با استفاده از عنوان

    :param title: عنوان وظیفه
    :return: سند وظیفه
    """
    document = await collection.find_one({'title': title})
    return document


async def get_all_todos():
    """
    دریافت همه وظایف

    :return: لیستی از وظایف
    """
    todos = []
    cursor = collection.find({})

    # پیمایش سندهای موجود در مجموعه
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def add_new_todo(todo: dict):
    """
    ایجاد یک وظیفه جدید

    :param todo: مدل وظیفه
    :return: سند وظیفه افزوده شده
    """
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo_description(title: str, desc: str):
    """
    بروزرسانی وظیفه

    :param title: عنوان وظیفه
    :param desc: توضیحات جدید
    :return: سند وظیفه بروزرسانی شده
    """
    await collection.update_one({'title': title}, {'$set': {'description': desc}})
    document = await collection.find_one({'title': title})
    return document


async def delete_todo_by_title(title: str):
    """
    حذف وظیفه

    :param title: عنوان وظیفه
    :return: موفقیت یا شکست حذف وظیفه
    """
    await collection.delete_one({'title': title})
    return True
