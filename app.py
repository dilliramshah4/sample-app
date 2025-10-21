from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Hello from Dr. ViKi DevOps Pipeline!</h1>
    <p>Current timestamp: {timestamp}</p>
    <p>Hostname: {os.environ.get('HOSTNAME', 'localhost')}</p>
    """

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
