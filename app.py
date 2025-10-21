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

@app.route('/metrics')
def metrics():
    return """# HELP flask_app_up Application status
# TYPE flask_app_up gauge
flask_app_up 1
# HELP flask_app_requests_total Total requests
# TYPE flask_app_requests_total counter
flask_app_requests_total 100
# HELP flask_app_response_time Response time in seconds
# TYPE flask_app_response_time gauge
flask_app_response_time 0.05
""", 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
