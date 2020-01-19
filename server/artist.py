'''
from server.utils import *
from flask import request
from flask import Blueprint

artist_routes = Blueprint('artist_routes', __name__)


@artist_routes.route('/api/artist/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    return jsonify([
  {
    "artist_country_id": "US",
    "artist_country_name": "United States",
    "artist_id": 44890,
    "artist_name": "Kings of Leon",
    "artist_rating": 81,
    "total_tracks_in_charts": 6,
    "unique_country_charts": 3
  }
])


@artist_routes.route('/api/artist_tracks/<artist_id>', methods=['GET'])
def get_tracks_by_artist(artist_id):
    return jsonify([
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
])


@artist_routes.route('/api/artist_charts/<artist_id>', methods=['GET'])
def get_charts_by_artist(artist_id):
    return jsonify([
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
])


@artist_routes.route('/api/similar_artists/<artist_id>', methods=['GET'])
def get_similar_artists(artist_id):
    return jsonify([
  {
    "artist_id": 7521,
    "artist_name": "Red Hot Chili Peppers"
  },
  {
    "artist_id": 1039,
    "artist_name": "Coldplay"
  },
  {
    "artist_id": 44890,
    "artist_name": "Kings of Leon"
  },
  {
    "artist_id": 512390,
    "artist_name": "The Rumour Said Fire"
  },
  {
    "artist_id": 70787,
    "artist_name": "The Killers"
  },
  {
    "artist_id": 106606,
    "artist_name": "Feist"
  },
  {
    "artist_id": 340352,
    "artist_name": "Lykke Li"
  },
  {
    "artist_id": 96,
    "artist_name": "The Cranberries"
  },
  {
    "artist_id": 416,
    "artist_name": "The Cure"
  },
  {
    "artist_id": 13895270,
    "artist_name": "Imagine Dragons"
  },
  {
    "artist_id": 210475,
    "artist_name": "Up Dharma Down"
  },
  {
    "artist_id": 349065,
    "artist_name": "Jamie Woon"
  },
  {
    "artist_id": 32364,
    "artist_name": "M83"
  },
  {
    "artist_id": 10528,
    "artist_name": "Gossip"
  },
  {
    "artist_id": 14344136,
    "artist_name": "American Authors"
  },
  {
    "artist_id": 13899662,
    "artist_name": "Willow"
  },
  {
    "artist_id": 8891,
    "artist_name": "Gorillaz"
  },
  {
    "artist_id": 27804801,
    "artist_name": "KALEO"
  },
  {
    "artist_id": 26475844,
    "artist_name": "Kwabs"
  },
  {
    "artist_id": 25781276,
    "artist_name": "Rag'n'Bone Man"
  },
  {
    "artist_id": 24444227,
    "artist_name": "Glass Animals"
  },
  {
    "artist_id": 14358589,
    "artist_name": "Cigarettes After Sex"
  },
  {
    "artist_id": 33932733,
    "artist_name": "King Gnu"
  },
  {
    "artist_id": 29247465,
    "artist_name": "Billie Eilish"
  },
  {
    "artist_id": 27926347,
    "artist_name": "Gerry Cinnamon"
  },
  {
    "artist_id": 35293137,
    "artist_name": "The FAIM"
  },
  {
    "artist_id": 13805436,
    "artist_name": "Lana Del Rey"
  },
  {
    "artist_id": 33091369,
    "artist_name": "Shatta Wale"
  },
  {
    "artist_id": 24676820,
    "artist_name": "SHAED"
  },
  {
    "artist_id": 93674,
    "artist_name": "LP"
  },
  {
    "artist_id": 31861215,
    "artist_name": "Dominic Fike"
  },
  {
    "artist_id": 37052122,
    "artist_name": "Hindia"
  },
  {
    "artist_id": 36235669,
    "artist_name": "Lil Nas X"
  },
  {
    "artist_id": 38851741,
    "artist_name": "BENEE"
  },
  {
    "artist_id": 37843472,
    "artist_name": "Tones and I"
  },
  {
    "artist_id": 36940461,
    "artist_name": "Tems"
  },
  {
    "artist_id": 24396907,
    "artist_name": "Milky Chance"
  },
  {
    "artist_id": 40355032,
    "artist_name": "Elaine"
  },
  {
    "artist_id": 29695422,
    "artist_name": "Kofi Kinaata"
  }
])


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
