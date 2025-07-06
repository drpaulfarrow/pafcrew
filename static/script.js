document.addEventListener("DOMContentLoaded", function() {
    fetchTasks();

    function fetchTasks() {
        fetch('/tasks')
            .then(response => response.json())
            .then(data => {
                const taskList = document.getElementById('task-list');
                taskList.innerHTML = '';
                data.forEach(task => {
                    const li = document.createElement('li');
                    li.textContent = task.task;
                    li.className = task.completed ? 'completed' : '';
                    li.addEventListener('click', () => markComplete(task.id));
                    taskList.appendChild(li);
                });
            });
    }
  
    window.addTask = function() {
        const newTaskInput = document.getElementById('new-task');
        const task = newTaskInput.value.trim();
        if (!task) return;

        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({task: task})
        })
        .then(response => response.json())
        .then(data => {
            newTaskInput.value = '';
            fetchTasks();
        });
    }

    function markComplete(taskId) {
        fetch(`/tasks/${taskId}`, {
            method: 'PUT'
        })
        .then(response => response.json())
        .then(data => {
            fetchTasks();
        });
    }
});
```