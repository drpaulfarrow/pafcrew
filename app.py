Sure! Below are the three required files for a minimal Flask app:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from AI Agent"

if __name__ == '__main__':
    app.run(debug=True)
```
