from flask import Flask, render_template
from flask_cors import CORS
from data_fetch.data_fetch_routes import data_fetch_routes
from web_app.app_routes import app_routes
from web_app.app_logic import *
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


@app.route('/artist/<track_id>')
def track(track_id):
    render_template("track.html", track_id=track_id)


# --------------- TODO - Delete the following routes ---------------- #
@app_routes.route('/show/<tab_name>/<limit>')
def show_table(tab_name, limit=100):
    rows = get_all_from_table(tab_name, limit)
    return render_template(template_name_or_list="old/base.html", rows=rows, title=tab_name)


@app_routes.route('/test')
def test():
    return render_template(template_name_or_list="old/charts_albums.html", base_url=BASE_URL)
# -------------------------------------------------------------------- #


if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=True)
