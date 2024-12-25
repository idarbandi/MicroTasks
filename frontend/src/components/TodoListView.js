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

import React from 'react';
import TodoItem from './Todo';
import './TodoListView.css'; // Import the CSS file for additional styling

/**
 * کامپوننت لیست وظایف
 *
 * @param {Array} props.todoList - لیست وظایف
 * @returns {JSX.Element} - لیستی از آیتم‌های وظیفه
 */
export default function TodoListView(props) {
  const todoList = props.todoList;
  const todoItems = todoList.map((todo, index) => <TodoItem key={index} todo={todo} />);

  return (
    <div className="todo-list-container">
      <ul className="todo-list">{todoItems}</ul>
    </div>
  );
}
