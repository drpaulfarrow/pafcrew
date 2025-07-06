```
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messaging

# Root route
@app.route('/')
def index():
    return render_template('index.html')

# Error handling example
@app.errorhandler(404)
def page_not_found(e):
    flash('Page not found. Redirecting to home.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
