from server.utils import *
from flask import request
from flask import Blueprint

artist_routes = Blueprint('artist_routes', __name__)


@artist_routes.route('/api/artist/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    return [
  {
    "artist_country_id": "US",
    "artist_country_name": "United States",
    "artist_id": 44890,
    "artist_name": "Kings of Leon",
    "artist_rating": 81,
    "total_tracks_in_charts": 6,
    "unique_country_charts": 3
  }
]


@artist_routes.route('/api/artist_tracks/<artist_id>', methods=['GET'])
def get_tracks_by_artist(artist_id):
    return [
  {
    "album_id": 10872038,
    "album_name": "Only By the Night",
    "artist_id": 44890,
    "artist_name": "Kings of Leon",
    "genre_id": 20,
    "genre_name": "Alternative",
    "genre_parent_id": 34,
    "track_id": 7562165,
    "track_name": "Use Somebody",
    "track_release_date": "Fri, 22 Nov 2019 20:44:10 GMT"
  },
  {
    "album_id": 10872038,
    "album_name": "Only By the Night",
    "artist_id": 44890,
    "artist_name": "Kings of Leon",
    "genre_id": 20,
    "genre_name": "Alternative",
    "genre_parent_id": 34,
    "track_id": 80160343,
    "track_name": "Sex on Fire",
    "track_release_date": "Fri, 22 Nov 2019 20:34:22 GMT"
  }
]


@artist_routes.route('/api/artist_charts/<artist_id>', methods=['GET'])
def get_charts_by_artist(artist_id):
    return [
  {
    "album_name": "Only By the Night",
    "country_id": "DK",
    "country_name": "Denmark",
    "track_id": 7562165,
    "track_name": "Use Somebody",
    "track_rank": 99
  },
  {
    "album_name": "Only By the Night",
    "country_id": "PL",
    "country_name": "Poland",
    "track_id": 7562165,
    "track_name": "Use Somebody",
    "track_rank": 55
  },
  {
    "album_name": "Only By the Night",
    "country_id": "SE",
    "country_name": "Sweden",
    "track_id": 7562165,
    "track_name": "Use Somebody",
    "track_rank": 69
  },
  {
    "album_name": "Only By the Night",
    "country_id": "DK",
    "country_name": "Denmark",
    "track_id": 80160343,
    "track_name": "Sex on Fire",
    "track_rank": 91
  },
  {
    "album_name": "Only By the Night",
    "country_id": "PL",
    "country_name": "Poland",
    "track_id": 80160343,
    "track_name": "Sex on Fire",
    "track_rank": 50
  },
  {
    "album_name": "Only By the Night",
    "country_id": "SE",
    "country_name": "Sweden",
    "track_id": 80160343,
    "track_name": "Sex on Fire",
    "track_rank": 75
  }
]


@artist_routes.route('/api/similar_artists/<artist_id>', methods=['GET'])
def get_similar_artists(artist_id):
    return []


@artist_routes.route('/api/artists', methods=['GET'])
def get_all_artists():
    return get_all_from_table('Artists')


'''
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
    query = "select a.*, c.country_name as artist_country_name, " \
            "       count(ch.country_id) as total_tracks_in_charts," \
            "       count(distinct ch.country_id) as unique_country_charts " \
            " from Artists a " \
            " left join Tracks t on t.artist_id = a.artist_id" \
            " left join Charts ch on ch.track_id = t.track_id " \
            " left join Countries c on c.country_id = a.artist_country_id " \
            "where a.artist_id = %s " \
            "group by a.artist_id, a.artist_name, a.artist_country_id, a.artist_rating, c.country_name"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/artist_tracks/<artist_id>', methods=['GET'])
def get_tracks_by_artist(artist_id):
    """
    :param artist_id
    :return: tracks: json of the artist's tracks in each chart including chart appearances
    """
    query = "select * from TracksView where artist_id = %s"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/artist_charts/<artist_id>', methods=['GET'])
def get_charts_by_artist(artist_id):
    """
    :param artist_id
    :return: tracks: json of the artist's tracks in each chart including chart appearances
    """
    query = "select t.track_id, t.album_name, t.track_name, c.country_id, c.country_name, ch.track_rank "\
            " from TracksView t"\
            " left join Charts ch on ch.track_id = t.track_id "\
            " left join Countries c on ch.country_id = c.country_id "\
            "where artist_id = %s;"
    args = (artist_id, )
    return query_to_json(query, args)


@artist_routes.route('/api/similar_artists/<artist_id>', methods=['GET'])
def get_similar_artists(artist_id):
    """
    :param artist_id
    :return: List of similar artists
    """
    query = "SELECT DISTINCT a1.artist_name "\
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


@artist_routes.route('/api/artists', methods=['GET'])
def get_all_artists():
    return get_all_from_table('Artists')
'''