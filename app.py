from flask import Flask
import requests
import time

app = Flask(__name__)

@app.route('/health')
def health_check():
    return {'status': 'OK'}, 200

@app.route('/')
def hello_world():
    return 'Hello, World! This is version 2 - with healh check 2'


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=8082)



while True:
    response = requests.get('http://localhost:8082/health')
    if response.status_code == 200:
        print('Flask app is healthy')
    else:
        print('Flask app is not healthy')
    time.sleep(30)
