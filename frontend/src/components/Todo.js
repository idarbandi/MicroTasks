import axios from 'axios';
import './TodoItem.css'; // Import the CSS file

function TodoItem(props) {
  const zapTodo = (title) => {
    axios.delete(`http://localhost:8000/api/todo/${title}`).then((res) => console.log(res.data));
  };

  return (
    <div className="todo-item mx-auto">
      <div className="todo-text">
        <span>{props.todo.title}:</span>
        <span id="toDodesc">{props.todo.description}:</span>
        <div className="container mt-5">
          {' '}
          <div id="buttonContainer">
            <button
              id="transformButton"
              className="btn btn-outline-success my-2 mx-2 delete-btn"
              onClick={(e) => (window.location += 'edit=' + props.todo.title)}
            >
              Edit
            </button>
            <button onClick={() => zapTodo(props.todo.title)} className="btn btn-outline-danger my-2 mx-2 delete-btn">
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TodoItem;
