import traceback
from database import sql_executor
from flask import jsonify


def get_all_countries():
    return get_all_from_table('Countries', 10000)


def get_all_artists():
    return get_all_from_table('Artists', 10000)


def search_track(by_lyrics=False, search_text="", from_date=None, to_date=None,
                 genre=None, album=None, artist=None):
    """
    :param by_lyrics: True iff searching lyrics, otherwise searching track name
    :param search_text: Text to search songs by
    :param from_date: Optional
    :param to_date: Optional
    :param genre: Optional
    :param album: Optional
    :param artist: Optional
    :return: List of tracks that match the above conditions
    """
    query = "select t.*, ar.artist_name, al.album_name, g.genre_name" \
            "  from Tracks t" \
            "  join Albums al on al.album_id = t.album_id and ({ALBUM_FILTER})" \
            "  join Artist ar on ar.artist_id = t.artist_id and ({ARTIST_FILTER}) " \
            "  join Genres g on g.genre = g.genre and ({GENRE_FILTER}) " \
            " where ({DATE_FILTER})" \
            "   and ({TEXT_FILTER})"

    args = []
    date_filter, album_filter, genre_filter, artist_filter = "1=1", "1=1", "1=1", "1=1"
    if album is not None:
        album_filter = 'al.album_name = %(album)s'
        args.append(album)

    if artist is not None:
        artist_filter = 'ar.artist_name = %(artist)s'
        args.append(artist)

    if genre is not None:
        genre_filter = 'g.genre_name = %(genre)s'
        args.append(genre)

    if from_date is not None and to_date is not None:
        date_filter = 'track_release date between %(from_date)s and %(to_date)s'
        args += [from_date, to_date]

    if by_lyrics:
        text_filter = " track_lyrics like '%'||%(text)s||'%'"
    else:
        text_filter = " track_name like '%'||%(text)s||'%'"
    args.append(search_text)

    query = query.format(DATE_FILTER=date_filter,
                         ALBUM_FILTER=album_filter,
                         ARTIST_FILTER=artist_filter,
                         GENRE_FILTER=genre_filter,
                         TEXT_FILTER=text_filter)

    return query_to_json(query=query, args=tuple(args))


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

