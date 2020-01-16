from flask import Flask, render_template
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
def home():
    return render_template("index.html")


@app.route('/artist/<artist_id>')
def artist(artist_id):
    return render_template("artist.html", artist_id=artist_id)


if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=True)
