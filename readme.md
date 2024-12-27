# 🗒️ MicroTasks

**MicroTasks** یک برنامه لیست کارهای ساده و موثر که با **FastAPI** و **React** ساخته شده است 📋🚀

## تولید کننده
این پروژه توسط `idarbandi` توسعه داده شده است.

- **ایمیل**: [darbandidr99@gmail.com](mailto:darbandidr99@gmail.com)
- **گیت‌هاب**: [idarbandi](https://github.com/idarbandi)

---

## 🛠️ ویژگی‌ها

- مدیریت کارها با امکان افزودن، حذف و نمایش لیست کارها
- رابط کاربری ساده و زیبا با استفاده از React
- پشتیبانی از تمام HTTP متدها با استفاده از FastAPI
- کانفیگ CORS برای دسترسی امن از همه‌ی منابع

---

## 🚀 شروع کار

این راهنما به شما کمک می‌کند تا پروژه را به صورت محلی روی سیستم خود راه‌اندازی کنید.

### پیش‌نیازها

- **Docker** و **Docker Compose**
- **Node.js** (اگر Docker استفاده نمی‌کنید)
- **Python 3.x**

### نصب

1. **کلون کردن مخزن**

   ```bash
   git clone https://github.com/idarbandi/MicroTasks.git
   cd MicroTasks
راه‌اندازی با Docker

bash
docker-compose up --build
نصب بدون Docker
نصب وابستگی‌ها برای Backend

bash
cd backend
python -m venv env
source env/bin/activate  # در ویندوز: .\env\Scripts\activate
pip install -r requirements.txt
اجرا کردن Backend

bash
uvicorn main:app --reload
نصب وابستگی‌ها برای Frontend

bash
cd ../frontend
npm install
اجرا کردن Frontend

bash
npm start
📄 استفاده
افزودن وظیفه

به /api/todo درخواست POST ارسال کنید با بدنه‌ای به صورت زیر:

json
{
  "title": "عنوان وظیفه",
  "description": "توضیحات وظیفه"
}
حذف وظیفه

به /api/todo/{title} درخواست DELETE ارسال کنید.

نمایش لیست وظایف

به /api/todo درخواست GET ارسال کنید.

🐳 Docker Configuration
Dockerfile برای Backend
Dockerfile
# استفاده از یک تصویر رسمی پایتون به عنوان تصویر اصلی
FROM python:3.11-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های نیازمندی‌ها
COPY requirements.txt .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کدهای برنامه
COPY . .

# پورت مورد نیاز
EXPOSE 80

# اجرای برنامه
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
Dockerfile برای Frontend
Dockerfile
# استفاده از نود به عنوان تصویر اصلی
FROM node:16-alpine

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های نیازمندی‌ها
COPY package*.json ./

# نصب وابستگی‌ها
RUN npm install

# کپی کردن بقیه کدهای برنامه
COPY . .

# ساخت برنامه
RUN npm run build

# پورت مورد نیاز
EXPOSE 3000

# اجرای برنامه
CMD ["serve", "-s", "build"]
Docker Compose Configuration
yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "80:80"
    volumes:
      - ./backend:/app
    environment:
      - PYTHONPATH=/app
    command: uvicorn main:app --host 0.0.0.0 --port 80

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
    environment:
      - CHOKIDAR_USEPOLLING=true
    command: serve -s build
📃 مجوز
این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر، فایل LICENSE را مشاهده کنید.

🤝 همکاری
در صورتی که تمایل دارید در توسعه این پروژه شرکت کنید، خوشحال می‌شویم که درخواست‌های تغییر (Pull Requests) شما را دریافت کنیم. همچنین می‌توانید هر گونه مشکل یا پیشنهاد را از طریق Issues مطرح کنید.

📞 تماس
برای هر گونه سوال یا توضیحات بیشتر، لطفاً با ایمیل darbandidr99@gmail.com در ارتباط باشید.

📦 وابستگی‌ها
FastAPI

Uvicorn

React

Axios

Docker

Docker Compose


You can copy and paste this `README.md` into your project. If you need any further assistance or have more questions, feel free to let me know! 🚀😊
