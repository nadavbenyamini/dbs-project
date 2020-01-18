from flask import Flask, render_template
from flask_cors import CORS
from data_fetch.data_fetch_routes import data_fetch_routes
from server.country import country_routes
from server.track import track_routes
from server.artist import artist_routes
from config import *

app = Flask(__name__)
CORS(app)
app.register_blueprint(data_fetch_routes)
app.register_blueprint(country_routes)
app.register_blueprint(track_routes)
app.register_blueprint(artist_routes)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/artist/<artist_id>')
def artist(artist_id):
    return render_template("artist.html", artist_id=artist_id)


@app.route('/track/<track_id>')
def track(track_id):
    return render_template("track.html", track_id=track_id)


@app.route('/country/<country_id>')
def country(country_id):
    return render_template("country.html", country_id=country_id)


if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=True)
