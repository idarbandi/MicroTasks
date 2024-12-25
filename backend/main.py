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

from database import (add_new_todo, delete_todo_by_title, get_all_todos,
                      get_todo_by_title, update_todo_description)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Todo

# شیء برنامه فست‌API
app = FastAPI()

# مبدا‌های مجاز
origins = ['http://localhost:3000']

# افزودن میان‌افزار CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE", "PUT"],
    allow_headers=["*"],
    max_age=3600,
)

# تست پاسخگویی سرور


@app.get('/')
def read_root():
    """
    مسیری برای تست پاسخگویی سرور
    """
    return {'Hello world'}

# مسیر‌ها


@app.get('/api/todo')
async def get_todo():
    """
    دریافت همه وظایف
    """
    response = await get_all_todos()
    return response


@app.get('/api/todo/{title}', response_model=Todo)
async def get_todo_by_id(title: str):
    """
    دریافت یک وظیفه بر اساس عنوان

    :param title: عنوان وظیفه
    :return: جزئیات وظیفه
    """
    response = await get_todo_by_title(title)
    if response:
        return response
    raise HTTPException(404, f'وظیفه‌ای با این عنوان وجود ندارد: {title}')


@app.post('/api/todo', response_model=Todo)
async def post_todo(todo: Todo):
    """
    افزودن یک وظیفه جدید

    :param todo: مدل وظیفه
    :return: وظیفه افزوده شده
    """
    response = await add_new_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, 'مشکلی پیش آمده است')


@app.put('/api/todo/{title}', response_model=Todo)
async def put_todo(title: str, desc: str):
    """
    بروزرسانی یک وظیفه

    :param title: عنوان وظیفه
    :param desc: توضیحات جدید
    :return: وظیفه بروزرسانی شده
    """
    response = await update_todo_description(title, desc)
    if response:
        return response
    raise HTTPException(404, f'وظیفه‌ای با این عنوان وجود ندارد: {title}')


@app.delete('/api/todo/{title}')
async def delete_todo(title: str):
    """
    حذف یک وظیفه

    :param title: عنوان وظیفه
    :return: پیام موفقیت آمیز بودن حذف وظیفه
    """
    response = await delete_todo_by_title(title)
    if response:
        return 'وظیفه با موفقیت حذف شد'
    raise HTTPException(404, f'وظیفه‌ای با این عنوان وجود ندارد: {title}')
