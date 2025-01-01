# 🗒️ MicroTasks

**MicroTasks** is a simple yet effective task management application built with **FastAPI** and **React** and **MongoDB** 📋🚀

## Creator
This project is developed by `idarbandi`.

- **Email**: [darbandidr99@gmail.com](mailto:darbandidr99@gmail.com)
- **GitHub**: [idarbandi](https://github.com/idarbandi)

---

## 🛠️ Features

- Manage tasks with the ability to add, delete, and view tasks
- Simple and elegant user interface with React
- Support for all HTTP methods using FastAPI
- CORS configuration for secure access from all origins

---

## 🚀 Getting Started

This guide will help you get the project up and running on your local machine.

### Prerequisites

- **Docker** and **Docker Compose**
- **Node.js** (if not using Docker)
- **Python 3.x**

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/idarbandi/MicroTasks.git
   cd MicroTasks
Start with Docker

bash
docker-compose up --build
Installation without Docker
Install dependencies for Backend

bash
cd backend
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
pip install -r requirements.txt
Run Backend

bash
uvicorn main:app --reload
Install dependencies for Frontend

bash
cd ../frontend
npm install
Run Frontend

bash
npm start
📄 Usage
Add a task

Send a POST request to /api/todo with the following body:

json
{
  "title": "Task Title",
  "description": "Task Description"
}
Delete a task

Send a DELETE request to /api/todo/{title}.

View task list

Send a GET request to /api/todo.

🐳 Docker Configuration
Dockerfile for Backend
Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
Dockerfile for Frontend
Dockerfile
# Use an official Node runtime as a parent image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the app for production
RUN npm run build

# Install serve to serve the build files
RUN npm install -g serve

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Serve the app
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
📃 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
We welcome contributions to this project. If you would like to contribute, please fork the repository and make a pull request. You can also report any issues or suggest improvements through the Issues page.

📞 Contact
For any questions or further information, please contact me at darbandidr99@gmail.com.

📦 Dependencies
FastAPI

Uvicorn

React

Axios

Docker

Docker Compose
