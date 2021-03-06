from server.utils import *
from flask import Blueprint

country_routes = Blueprint('country_routes', __name__)


@country_routes.route('/api/country_genres/<country_id>', methods=['GET'])
def get_popular_genres(country_id):
    """
    :param country_id
    :return: List of popular genres in the country's charts
    """
    query = "SELECT g.genre_name, COUNT(g.genre_id) AS number_of_songs_in_chart "\
            "  FROM Charts c, Tracks t, Genres g "\
            " WHERE c.country_id = %s " \
            "   AND c.track_id = t.track_id " \
            "   AND t.genre_id = g.genre_id "\
            " GROUP BY g.genre_id "\
            " ORDER BY number_of_songs_in_chart DESC;"
    args = (country_id, )
    return query_to_json(query, args)


@country_routes.route('/api/country_artists/<country_id>', methods=['GET'])
def get_popular_artists(country_id):
    """
    :param country_id
    :return: List of popular artists in the country's charts
    """
    query = "SELECT a.artist_id, a.artist_name, COUNT(a.artist_id) AS number_of_songs_in_chart "\
            "  FROM Charts c, Tracks t, Artists a " \
            " WHERE c.country_id = %s " \
            "   AND c.track_id =t.track_id " \
            "   AND t.artist_id = a.artist_id " \
            " GROUP BY a.artist_id " \
            " ORDER BY number_of_songs_in_chart DESC "
    args = (country_id, )
    return query_to_json(query, args)


@country_routes.route('/api/country_tracks/<country_id>', methods=['GET'])
def get_tracks_by_country(country_id):
    """
    :param country_id
    :return: tracks: json of tracks from the country's chart
    """
    query = "select t.track_id, t.track_name, t.album_name, t.artist_id, t.artist_name, t.genre_name, " \
            "       t.track_release_date_formatted as track_release_date, c.*, ch.track_rank " \
            "  from Countries c " \
            "  join Charts ch on c.country_id = ch.country_id " \
            "  join TracksView t on t.track_id = ch.track_id " \
            " where c.country_id = %s "\
            " order by track_rank"
    args = (country_id, )
    return query_to_json(query, args)


@country_routes.route('/api/countries', methods=['GET'])
def get_all_countries():
    return get_all_from_table('Countries', order_by=2)
