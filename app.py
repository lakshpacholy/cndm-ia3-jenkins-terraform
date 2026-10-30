from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    build_num = os.environ.get('BUILD_NUMBER', 'Local')
    hostname = socket.gethostname()
    return f"<h1>Jenkins CI/CD Pipeline Success!</h1><p>Candidate: Laksh Pacholy</p><p>Build Number: {build_num}</p><p>Hostname: {hostname}</p>"

@app.route('/health')
def health():
    return {"status": "healthy"}

@app.route('/version')
def version():
    return {"version": "1.0.0"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
