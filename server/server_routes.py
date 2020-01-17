from flask import Blueprint
from flask import request
from server.track import *
from server.artist import *

api_routes = Blueprint('server_routes', __name__)

"""
This file is for defining the app's API routes
Internal logic, queries, etc. are in other places
"""


@api_routes.route('/api/track/<track_id>', methods=['GET'])
def get_track_by_id(track_id):
    return get_track(track_id)


@api_routes.route('/api/artist/<artist_id>', methods=['GET'])
def get_artist_by_id(artist_id):
    return get_artist(artist_id)


@api_routes.route('/api/search/track', methods=['GET'])
def search_tracks_route():
    params = request.args
    by_lyrics = params.get('by_lyrics', False)
    by_artist = params.get('by_artist', False)
    assert not by_lyrics or not by_artist  # Can't search by both...
    return search_track(by_lyrics=params.get('by_lyrics', False),
                        by_artist=params.get('by_artist', False),
                        search_text=params.get('search_text', None),
                        from_date=params.get('from_date', None),
                        to_date=params.get('to_date', None),
                        genre=params.get('genre', None),
                        album=params.get('album', None),
                        page_size=params.get('page_size', 100),
                        page_number=params.get('page_number', 1))


@api_routes.route('/api/search/artist', methods=['GET'])
def search_artist_route():
    params = request.args
    return search_artist(search_text=params.get('search_text', None),
                         page_size=params.get('page_size', 100),
                         page_number=params.get('page_number', 1))


@api_routes.route('/api/artists/<country_id>', methods=['GET'])
def country_artists(country_id):
    return get_artists_by_country_id(country_id)


@api_routes.route('/api/countries', methods=['GET'])
def api():
    return get_all_countries()


@api_routes.route('/api/country_tracks/<country_id>', methods=['GET'])
def country_tracks(country_id):
    return get_tracks_by_country(country_id)


@api_routes.route('/api/artist_tracks/<artist_id>', methods=['GET'])
def artist_tracks(artist_id):
    response = get_tracks_by_artist(artist_id)
    return response


@api_routes.route('/api/artists', methods=['GET'])
def get_artists():
    response = get_all_artists()
    return response


@api_routes.errorhandler(APIException)
def handle_error(error):
    response = error.to_json()
    response.status_code = error.status_code
    return response

