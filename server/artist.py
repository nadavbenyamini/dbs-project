from server.utils import *
from flask import request
from flask import Blueprint

artist_routes = Blueprint('artist_routes', __name__)


@artist_routes.route('/api/artist/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    """
    GETTER
    :param artist_id
    :return: Everything from Artists table
    """
    query = "select * from Artists where artist_id = %s"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/search/artist', methods=['GET'])
def search_artist_route():
    params = request.args
    return search_artist(search_text=params.get('search_text', None),
                         page_size=params.get('page_size', 100),
                         page_number=params.get('page_number', 1))


def search_artist(search_text="", page_size=100, page_number=1):
    """
    :param search_text: Text to search songs by
    :param page_size: Number of results to fetch
    :param page_number: Offset
    :return: List of artists that contain search_text in their name
    """
    query = "select * from Artists a where artist_name like %s"
    args = ('%'+search_text+'%', )
    return query_to_json(query, args, page_size=page_size, page_number=page_number)


@artist_routes.route('/api/artist_tracks/<artist_id>', methods=['GET'])
def get_tracks_by_artist(artist_id):
    """
    :param artist_id:
    :return: tracks: json of the artist's tracks
    """
    query = "select * " \
            "from Artists a, Tracks t, Albums al, Genres g "\
            "where a.artist_id = %s "\
            "and t.artist_id = a.artist_id and al.album_id=t.album_id and g.genre_id = t.genre_id "
    args = (int(artist_id), )
    return query_to_json(query, args)


@artist_routes.route('/api/artists', methods=['GET'])
def get_all_artists():
    return get_all_from_table('Artists', 10000)

