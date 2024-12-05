document.addEventListener('DOMContentLoaded', function() {
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');
    const todoBtn = document.getElementById('todo-btn');
    const themeBtn = document.getElementById('theme-toggle')

    let isDark = JSON.parse(localStorage.getItem('isDark')) || false;

    themeBtn.addEventListener('click', toggleTheme);
    todoBtn.addEventListener('click', addTodo);

    todoList.addEventListener('click', function(e) {
        if (e.target.closest('.delete-btn')) {
            const id = e.target.closest('.todo-item').dataset.id;
            const todoItem = e.target.closest('.todo-item');
            deleteTodo(id, todoItem);
        }
    })

    todoList.addEventListener('change', function(e) {
        if (e.target.closest('.checkbox')) {
            const id = e.target.closest('.todo-item').dataset.id;
            const completed = e.target.checked;
            toggleTodo(id, completed);
        }
    })

    async function addTodo() {
        const newTodoContent = todoInput.value.trim();

        if (newTodoContent) {
            const response = await fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ content: newTodoContent })
            });

            if (response.ok) {
                const newTodo = await response.json();
                renderNewTask(newTodo);
                todoInput.value = '';
            }
            else {
                console.error('Failed to create new task')
            }
        }
    }

    function renderNewTask(newTodo) {
        const todoItem = document.createElement('li');
        todoItem.classList.add('todo-item');
        todoItem.dataset.id = newTodo.id;
        todoItem.innerHTML = `
            <input type="checkbox" class='checkbox' ${newTodo.completed ? 'checked' : ''} data-id="${newTodo.id}">
            <span class='todo-content'>${newTodo.content}</span>
            <span class='task-date'>${newTodo.date_created.date()}</span>
            <button class='delete-btn'><i class="fas fa-trash"></i></button>
            `;
        todoList.appendChild(todoItem);
    }

    async function toggleTodo(id, completed) {
        const response = await fetch(`api/tasks/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ completed: completed })
        });

        if (response.ok) {
            const data = await response.json();
            const todoItem = document.querySelector(`.todo-item[data-id="${id}"]`);

            if (todoItem) {
                todoItem.classList.toggle('done', data.completed);
                console.log('Task status updated')
            }
            else {
                console.error('Task not found')
            }
        }
        else {
            console.error('Failed to update task status')
        }
    }

    async function deleteTodo(id, todoItem){
        const response = await fetch(`/api/tasks/${id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            todoItem.remove();
        }
        else (
            console.error('Failed to delete task')
        )
    }
    
    function toggleTheme() {
        isDark = !isDark;
        document.body.classList.toggle('dark-theme', isDark);
        themeBtn.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        localStorage.setItem('isDark', isDark);
    }

    function initTheme() {
        document.body.classList.toggle('dark-theme', isDark);
        themeBtn.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    }

    initTheme();
})