from server.utils import *
from flask import request
from flask import Blueprint

track_routes = Blueprint('track_routes', __name__)


@track_routes.route('/api/track/<track_id>', methods=['GET'])
def get_track(track_id):
    """
    GETTER
    :param track_id
    :return: Everything from Tracks table
    """
    query = "select * from TracksView where track_id = %s"
    args = (track_id, )
    return query_to_json(query, args)


@track_routes.route('/api/similar_tracks/<track_id>', methods=['GET'])
def get_similar_tracks(track_id):
    """
    :param track_id
    :return: List of tracks similar to the input track according to genre and chart rankings
    """
    query = "SELECT DISTINCT t.* "\
            "FROM TracksView " \
            "   (SELECT MIN(c.track_rank) AS min_rank," \
            "           MAX(c.track_rank) AS max_rank " \
            "   FROM Charts c " \
            "   WHERE c.track_id = %s " \
            ") AS  min_max_rank " \
            "WHERE t.genre_id = " \
            "   (SELECT t2.genre_id " \
            "   FROM Tracks t2 " \
            "   WHERE  t2.track_id = %s) AND t.track_id != %s " \
            "     AND min_max_rank.max_rank >= " \
            "       (SELECT AVG(c3.track_rank) " \
            "           FROM Charts c3 " \
            "           WHERE c3.track_id=t.track_id) " \
            "     AND min_max_rank.min_rank <= " \
            "       (SELECT AVG(c4.track_rank) " \
            "           FROM Charts c4 " \
            "           WHERE c4.track_id=t.track_id ); "
    args = (track_id, track_id, track_id)
    return query_to_json(query, args)


@track_routes.route('/api/search/track', methods=['GET'])
def search_tracks_route():
    params = request.args
    return search_track(search_by=params.get('search_by', False),
                        search_text=params.get('search_text', None),
                        date_from=params.get('date_from', None),
                        date_to=params.get('date_to', None),
                        genre_id=params.get('genre_id', None),
                        page_size=params.get('page_size', 100),
                        page_number=params.get('page_number', 1))


def search_track(search_by=None, search_text=None, date_from=None, date_to=None,
                 genre_id=None, page_size=100, page_number=1):
    """
    :param search_by: Textual search field ('track_name'/'artist_name'/'album_name'/'track_lyrics')
    :param search_text: Text to search songs by
    :param date_from: Optional (YYYY-mm-dd)
    :param date_to: Optional (YYYY-mm-dd)
    :param genre_id: Optional (exact ID from list, not free text.
                     Searching also parent id so e.g. 'rock' will return 'hard rock' tracks too
    :param page_size: Number of results to fetch
    :param page_number: Offset
    :return: List of tracks that match the above conditions
    """
    query = "select track_id, artist_id, track_name, album_name, artist_name, genre_name," \
            "       REPLACE(DATE_FORMAT(track_release_date, %s), '\\\\', '') as track_release_date " \
            "  from TracksView t" \
            " where ({DATE_FILTER})" \
            "   and ({GENRE_FILTER})" \
            "   and ({TEXT_FILTER})" \
            " order by artist_name, track_name" \
            " limit {LIMIT};"

    args = ["\\%M \\%d, \\%Y"]
    text_filter = date_filter = genre_filter = "1=1"

    if date_from is not None and date_to is not None:
        date_filter = 'track_release_date > %s and track_release_date < %s'
        args += [date_from.replace('-', '/'), date_to.replace('-', '/')]

    if genre_id is not None:
        try:
            genre_id = int(genre_id)
            genre_filter = "genre_id = %s or genre_parent_id = %s"
            args += [genre_id, genre_id]
        except ValueError:
            pass

    if search_text is not None:
        if search_by == 'track_lyrics':
            text_filter = "MATCH(track_lyrics) AGAINST (%s)"
            args.append(search_text)
        elif search_by == 'artist_name':
            text_filter = "artist_name like %s"
            args.append(search_text + "%")  # '%' only on the right to use index
        elif search_by == 'album_name':
            text_filter = "album_name like %s"
            args.append(search_text + "%")  # '%' only on the right to use index
        else:
            text_filter = "track_name like %s"
            args.append(search_text + "%")  # '%' only on the right to use index

    try:
        page_number = int(page_number)
        page_size = int(page_size)
        limit = '{}, {}'.format(page_size * (page_number - 1), page_size)
    except ValueError:
        limit = '1, 100000'

    query = query.format(DATE_FILTER=date_filter,
                         GENRE_FILTER=genre_filter,
                         TEXT_FILTER=text_filter,
                         LIMIT=limit)
    return query_to_json(query=query, args=tuple(args))
