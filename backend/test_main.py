import pytest
from httpx import AsyncClient
from main import Todo, app

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

# تست گرفتن لیست وظایف


@pytest.mark.asyncio
async def test_get_todos():
    """
    این تست بررسی می‌کند که آیا لیست وظایف به درستی بازگردانده می‌شود یا خیر.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/todo")
    assert response.status_code == 200
    assert response.json() == []

# تست افزودن وظیفه


@pytest.mark.asyncio
async def test_add_todo():
    """
    این تست بررسی می‌کند که آیا یک وظیفه به درستی افزوده می‌شود یا خیر.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        todo = {"title": "Test Todo", "description": "This is a test"}
        response = await ac.post("/api/todo", json=todo)
    assert response.status_code == 200
    assert response.json() == {"message": "Todo added successfully"}

# تست حذف وظیفه


@pytest.mark.asyncio
async def test_delete_todo():
    """
    این تست بررسی می‌کند که آیا یک وظیفه به درستی حذف می‌شود یا خیر.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        todo = {"title": "Test Todo", "description": "This is a test"}
        await ac.post("/api/todo", json=todo)
        response = await ac.delete("/api/todo/Test Todo")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted successfully"}
