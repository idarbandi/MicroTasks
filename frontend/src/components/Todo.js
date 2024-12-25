import axios from 'axios';
import './TodoItem.css'; // Import the CSS file

function TodoItem(props) {
  const zapTodo = (title) => {
    axios.delete(`http://localhost:8000/api/todo/${title}`).then((res) => console.log(res.data));
  };

  return (
    <div className="todo-item mx-auto">
      <p className="todo-text">
        <span>{props.todo.title}:</span>
        {props.todo.description}
        <button onClick={() => zapTodo(props.todo.title)} className="btn btn-outline-danger my-2 mx-2 delete-btn">
          Delete
        </button>
      </p>
    </div>
  );
}

export default TodoItem;
