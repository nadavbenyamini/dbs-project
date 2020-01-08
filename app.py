from flask import Flask
from routes.data_fetch_routes import data_fetch_routes
from routes.app_routes import app_routes

app = Flask(__name__)
app.register_blueprint(data_fetch_routes)
app.register_blueprint(app_routes)


@app.route('/')
def hello_world():
    return 'Hello World\n'


if __name__ == '__main__':
    app.run(port=5001, host="0.0.0.0", debug=True)
