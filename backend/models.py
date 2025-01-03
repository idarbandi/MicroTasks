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

from pydantic import BaseModel

class Todo(BaseModel):
    """
    کلاس مدل Todo برای نمایندگی وظایف در برنامه

    ویژگی‌ها:
        - title: عنوان وظیفه
        - description: توضیحات وظیفه
    """
    title: str
    description: str
