from flask import render_template
from flask import Blueprint
from flask import request
from web_app.track import *
from web_app.artist import *
from config import *

app_routes = Blueprint('app_routes', __name__)

"""
This file is for defining the app's API routes
Internal logic, queries, etc. are in other places
"""


@app_routes.route('/search/track')
def search_tracks_route():
    params = request.args
    assert 'search_text' in params
    return search_track(by_lyrics=params.get('by_lyrics', False),
                        search_text=params.get('search_text', None),
                        from_date=params.get('from_date', None),
                        to_date=params.get('to_date', None),
                        genre=params.get('genre', None),
                        album=params.get('album', None),
                        artist=params.get('artist', None))


@app_routes.route('/artists/<country_id>', methods=['GET'])
def country_artists(country_id):
    return get_artists_by_country_id(country_id)


@app_routes.route('/countries', methods=['GET'])
def all_countries():
    return get_all_countries()


@app_routes.route('/country_tracks/<country_id>', methods=['GET'])
def country_tracks(country_id):
    return get_tracks_by_country(country_id)


@app_routes.route('/artist_tracks/<artist_id>', methods=['GET'])
def artist_tracks(artist_id):
    response = get_tracks_by_artist(artist_id)
    return response


@app_routes.route('/tracks/<track_id>', methods=['GET'])
def get_track(track_id):
    response = get_track_by_id(track_id)
    return response


@app_routes.route('/artists', methods=['GET'])
def get_artists():
    response = get_all_artists()
    return response


@app_routes.route('/show/<tab_name>/<limit>')
def show_table(tab_name, limit=100):
    rows = get_all_from_table(tab_name, limit)
    return render_template(template_name_or_list="old/base.html", rows=rows, title=tab_name)


@app_routes.route('/test')
def temp():
    return render_template(template_name_or_list="charts_albums.html", base_url=BASE_URL)


@app_routes.errorhandler(APIException)
def handle_error(error):
    response = error.to_json()
    response.status_code = error.status_code
    return response

