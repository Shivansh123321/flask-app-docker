from flask import Flask
import logging

app = Flask(__name__)

@app.route('/health')
def health_check():
    logging.info("in health check")
    return {'status': 'OK'}, 200

@app.route('/')
def hello_world():
    logging.info("in hellow world")
    return 'Hello, World! This is version 2 - with healh check 3'


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=8082)


