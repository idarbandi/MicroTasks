# استفاده از یک تصویر اصلی نود برای اجرای برنامه ریکت
FROM node:16-alpine

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل package.json و package-lock.json به داخل کانتینر
COPY package*.json ./

# نصب وابستگی‌ها
RUN npm install

# کپی کردن بقیه کدهای برنامه
COPY . .

# ساخت برنامه برای محیط تولید
RUN npm run build

# استفاده از سرور ساده برای سرو برنامه‌های استاتیک
RUN npm install -g serve

# فراهم کردن پورت 3000 برای دسترسی به برنامه
EXPOSE 3000

# اجرای برنامه
CMD ["serve", "-s", "build"]
