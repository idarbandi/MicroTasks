# استفاده از یک تصویر اصلی پایتون به عنوان تصویر والد
FROM python:3.11-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل نیازمندی‌ها به داخل کانتینر
COPY requirements.txt .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن بقیه کدهای برنامه
COPY . .

# فراهم کردن پورت 80 برای دسترسی از خارج کانتینر
EXPOSE 80

# تعریف متغیر محیطی
ENV PYTHONPATH=/app

# اجرای سرور FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
