from server.utils import *
from flask import request
from flask import Blueprint

artist_routes = Blueprint('artist_routes', __name__)


@artist_routes.route('/api/artist/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    """
    :param artist_id
    :return: Basic information and statistics about artist
    """
    query = "select a.artist_id, a.artist_name, a.artist_country_id, ROUND(a.artist_rating/20,0) as artist_rating," \
            "       c.country_name as artist_country_name, " \
            "       count(ch.country_id) as total_tracks_in_charts," \
            "       count(distinct ch.country_id) as unique_country_charts " \
            " from Artists a " \
            " left join Tracks t on t.artist_id = a.artist_id" \
            " left join Charts ch on ch.track_id = t.track_id " \
            " left join Countries c on c.country_id = a.artist_country_id " \
            "where a.artist_id = %s " \
            "group by a.artist_id, a.artist_name, a.artist_country_id, a.artist_rating, c.country_name;"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/artist_tracks/<artist_id>', methods=['GET'])
def get_top_tracks_by_artist(artist_id):
    """
    :param artist_id
    :return: tracks: Top tracks according to the overall ranking in charts
    """
    query = " SELECT t.track_id, track_name, album_name, SUM(101-c.track_rank) AS track_ranking, "\
            "        track_release_date_formatted as track_release_date, genre_name"\
            "   FROM TracksView t, Charts c "\
            "  WHERE t.track_id = c.track_id AND "\
            "		 t.artist_id = %s "\
            "  GROUP BY t.track_id "\
            "  ORDER BY track_ranking DESC;"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/artist_charts/<artist_id>', methods=['GET'])
def get_top_countries_by_artist(artist_id):
    """
    :param artist_id
    :return: tracks: Top countries by artist
    """
    query = "select cr.country_id," \
            "       cr.country_name, "\
            "       cr.population AS country_population, "\
            "       SUM(101-ch.track_rank) AS total_rank_in_country, "\
            "       COUNT(t.track_id) AS number_of_songs_on_country_chart "\
            "  from TracksView t "\
            "  join Charts ch on ch.track_id = t.track_id "\
            "  join Countries cr on cr.country_id = ch.country_id "\
            " where artist_id = %s " \
            " group by 1, 2, 3 " \
            " order by total_rank_in_country desc;"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/similar_artists/<artist_id>', methods=['GET'])
def get_similar_artists(artist_id):
    """
    :param artist_id
    :return: List of similar artists
    """
    query = "SELECT DISTINCT a1.artist_id, a1.artist_name "\
            "FROM Artists a1, Tracks t1, Genres g1, "\
            "   (SELECT MAX(c.track_rank) AS max_rating , MIN(c.track_rank) AS min_rating "\
            "   FROM Artists a , Tracks t ,Charts c "\
            "   WHERE a.artist_id = t.artist_id AND "\
            "   c.track_id = t.track_id AND "\
            "   a.artist_id = %s) AS min_max_rating "\
            "WHERE a1.artist_id = t1.artist_id AND "\
            "t1.genre_id =g1.genre_id AND "\
            "g1.genre_id IN " \
            "   (SELECT DISTINCT  g0.genre_id "\
            "   FROM Artists a0, Tracks t0, Genres g0 "\
            "   WHERE a0.artist_id = t0.artist_id " \
            "     AND t0.genre_id = g0.genre_id " \
            "     AND a0.artist_id = %s) " \
            "AND t1.track_rating>=min_max_rating.min_rating " \
            "AND t1.track_rating<=min_max_rating.max_rating;"
    args = (artist_id, artist_id)
    return query_to_json(query, args)
