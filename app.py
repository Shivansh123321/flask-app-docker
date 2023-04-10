from flask import Flask
from flask import Blueprint

app = Flask(__name__)
health_bp = Blueprint('health', __name__)


@app.route('/')
def hello_world():
    return 'Hello, World! This is version 2'

@health_bp.route('/healthcheck')
def health_check():
    return 'OK', 200

def initialize_app(flask_app):
    app.register_blueprint(health_bp)


if __name__ == "__main__":
    initialize_app(app)
    app.run(host='0.0.0.0',debug=True,port=8082)
    

