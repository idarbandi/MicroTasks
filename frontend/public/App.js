/**
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
 */

import './App.css';
import { useState, useEffect } from 'react';
import TodoListView from './components/TodoListView';
import axios from 'axios';

// ایمپورت بوت‌استرپ
import 'bootstrap/dist/css/bootstrap.min.css';

/**
 * کامپوننت اصلی برنامه
 * @returns {JSX.Element}
 */
function MainApp() {
  // متغیرهای ذخیره‌سازی لیست وظایف، عنوان و توضیحات
  let paramsString ;
  let searchParams = new URLSearchParams(paramsString);
  const [todoList, setTodoList] = useState([]);
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');

  // useEffect برای دریافت همه وظایف
  useEffect(() => {
    window.location.pathname.startsWith('http://localhost:3000/edit') ? paramsString = window.location.pathname : null
    fetchTodos();
  }, []);

  /**
   * دریافت وظایف از API
   */
  const fetchTodos = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/todo');
      setTodoList(response.data);
    } catch (error) {
      console.error('خطایی در دریافت وظایف رخ داد', error);
    }
  };

  /**
   * افزودن یک وظیفه جدید
   */
  const addTask = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/todo', { title, description: desc });
      console.log(response);
      fetchTodos(); // Refresh the list after adding a task
    } catch (error) {
      console.error('خطایی در افزودن وظیفه رخ داد', error);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>MicroTasks</h1>
        <div className="tech-icons">
          <img src="mongo_icon.png" alt="MongoDB" />
          <img src="frontend/fastapi_icon.png" alt="FastAPI" />
          <img src="react_icon.png" alt="React" />
        </div>
      </header>
      <main>
        <div className="todo-manager">
          <h1 className="task-manager-header">Task Manager</h1>
          <h6 className="stack-info">FASTAPI - React - MongoDB</h6>
          <div className="card-body"></div>
          <h5 className="add-task-header">Add Your Task Below</h5>
          <span className="task-inputs">
            <input
              className="mb-2 form-control"
              onChange={(event) => setTitle(event.target.value)}
              placeholder="Title"
            />
            <input
              className="mb-2 form-control"
              onChange={(event) => setDesc(event.target.value)}
              placeholder="Description"
            />
            <button className="btn custom-save-btn" onClick={addTask}>
              Save Task
            </button>
          </span>
        </div>
        <div className="todo-list-container mt-5">
          <h5 className="your-tasks-header">Your Tasks</h5>
          <TodoListView todoList={todoList} />
        </div>
      </main>
      <footer className="app-footer">
        <p>&copy; 2024 MicroTasks. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default MainApp;
