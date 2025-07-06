```
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This will act as our database for this simple app
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task:
            tasks.append(new_task)
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
