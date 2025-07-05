```
# Flask To-Do List

This is a simple to-do list application built using Flask, a lightweight web application framework for Python. The app allows users to add and delete tasks from their to-do list.

## Features

- Add tasks
- Delete tasks

## Prerequisites

- Python 3.x installed on your machine

## Installation and Running

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```bash
    python app.py
    ```

4. Open your web browser and go to `http://127.0.0.1:5000` to use the to-do list app.

## Usage

- Enter a task name in the input box and click "Add" to add a new task.
- Click "Delete" next to a task to remove it from the list.
```

This setup provides a basic but functional to-do list application using Flask, including user interfaces for adding and deleting tasks. The example uses an in-memory list to store tasks, which means the tasks will be reset when the server restarts. For persistence, consider integrating a database.