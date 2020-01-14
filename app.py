from flask import Flask
from flask_cors import CORS
from data_fetch.data_fetch_routes import data_fetch_routes
from web_app.app_routes import app_routes
from config import *

# initialization

app = Flask(__name__)
CORS(app)
app.register_blueprint(data_fetch_routes)
app.register_blueprint(app_routes)


@app.route('/')
def hello_world():
    return 'Hello World\n'


if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=True)
