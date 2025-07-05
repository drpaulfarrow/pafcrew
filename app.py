To create a simple Flask-based to-do list app, here's the implementation including `app.py`, `requirements.txt`, and `README.md`.

```python
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        tasks.append(task_content)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

You'll also need a simple HTML template for displaying the tasks. Create a new folder named `templates`, and inside it create a file named `index.html` with the following content:

```html
<!doctype html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <form action="{{ url_for('add_task') }}" method="post">
        <input type="text" name="task" placeholder="Enter new task" required>
        <input type="submit" value="Add">
    </form>
    <ul>
        {% for task in tasks %}
        <li>
            {{ task }}
            <a href="{{ url_for('delete_task', task_id=loop.index0) }}">Delete</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```
