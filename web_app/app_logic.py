import traceback
from database import sql_executor
from flask import jsonify


def get_all_countries():
    """
    :return: JSON of Countries table
    """
    return get_all_from_table('Countries', 1000)


def get_all_artists():
    return get_all_from_table('Artists', 1000)



def get_tracks_by_country(country_id):
    """
    :param country_id:
    :return: tracks: json of tracks from the country's chart
    """
    query = "select t.*, c.*, ch.track_rank " \
            "  from Countries c " \
            "  join Charts ch " \
            "    on c.country_id = ch.country_id" \
            "  join Tracks t" \
            "    on t.track_id = ch.track_id" \
            " where c.country_id = %s" \
            " order by track_rank"
    args = (country_id, )  # Converting to tuple...
    return query_to_json(query, args)


def get_tracks_by_artist(artist_id):
    """
    :param artist_id:
    :return: tracks: json of the artist's tracks
    """
    query = "select * " \
            "from Artists a, Tracks t, Albums al, Genres g "\
            "where a.artist_id = %s "\
            "and t.artist_id = a.artist_id and al.album_id=t.album_id and g.genre_id = t.genre_id "
    args = (int(artist_id), )  # Converting to tuple...
    return query_to_json(query, args)


def get_tracks_by_id(track_id):
    query = "select * from Tracks t, Artists a where track_id = %s and t.artist_id = a.artist_id"
    args = int(track_id)
    return query_to_json(query, args)


def get_all_from_table(tab_name, limit):
    """
    An *UNSAFE* *TEMPORARY* method for testing
    # TODO - prevent SQL Injection (maybe make this a private method)
    :param tab_name: table in our DB
    :param limit: #rows
    :return: simple JSON of select * from tab_name
    """
    query = "select * from {} limit {}".format(tab_name, limit)
    db_results = sql_executor.select(query=query)
    return res_to_json(db_results)


# ------------------------------------------------------------------------------------------ #
# ---------------------------------  General Utilities ------------------------------------- #
# ------------------------------------------------------------------------------------------ #

def query_to_json(query, args=None):
    try:
        db_results = sql_executor.select(query=query, args=args)
        return res_to_json(db_results)
    except sql_executor.NoResultsException as e:
        raise APIException(e.message, status_code=404)
    except Exception as e:
        raise APIException(e.message, status_code=500)


def res_to_json(res):
    _rows = []
    headers = res['headers']
    for row in res['rows']:
        _rows.append({headers[i]: row[i] for i in range(len(headers))})
    return jsonify(_rows)


class APIException(Exception):
    """
    Customer error raising.
    For example wrong track id should be error 404 not 500
    """
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        print('Message: {}\n{}'.format(message, traceback.format_exc()))
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_json(self):
        return jsonify({'message': self.message})

