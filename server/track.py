from server.server_utils import *
from flask import request
from flask import Blueprint

track_routes = Blueprint('track_routes', __name__)


@track_routes.route('/api/track/<track_id>', methods=['GET'])
def get_track(track_id):
    """
    GETTER
    :param track_id
    :return: Everything from Track table
    """
    query = "select * from Track where track_id = %s"
    args = (track_id, )
    return query_to_json(query, args)


@track_routes.route('/api/similar_tracks/<track_id>', methods=['GET'])
def get_similar_tracks(track_id):
    query = "SELECT DISTINCT t.track_id,  t.track_name , a.artist_name,al.album_name, " \
            "genre_name AS track_genre, t.track_release_date " \
            "FROM Tracks t ,Artists a, Albums al, Genres g, " \
            "   (SELECT MIN(c.track_rank) AS min_rank," \
            "   MAX(c.track_rank) AS max_rank " \
            "   FROM Charts c " \
            "   WHERE c.track_id = %s " \
            ") AS  min_max_rank " \
            "WHERE a.artist_id = t.artist_id AND " \
            "al.album_id =t.album_id AND " \
            "g.genre_id =t.genre_id AND " \
            "t.genre_id = (SELECT t2.genre_id " \
            "FROM Tracks t2 " \
            "WHERE  t2.track_id = %s) AND " \
            "t.track_id != %s " \
            "AND min_max_rank.max_rank >= (SELECT AVG(c3.track_rank) " \
            "   FROM Charts c3 " \
            "   WHERE c3.track_id=t.track_id ) " \
            "AND min_max_rank.min_rank <= (SELECT AVG(c4.track_rank) " \
            "   FROM Charts c4 " \
            "   WHERE c4.track_id=t.track_id ); "
    args = (track_id, track_id, track_id)
    return query_to_json(query, args)


@track_routes.route('/api/search/track', methods=['GET'])
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


def search_track(by_lyrics=False, by_artist=False, search_text=None, from_date=None, to_date=None,
                 genre=None, album=None, page_size=100, page_number=1):
    """
    :param by_lyrics: True iff searching lyrics, otherwise searching track name
    :param by_artist: True iff searching tracks by artist name
    :param search_text: Text to search songs by
    :param from_date: Optional
    :param to_date: Optional
    :param genre: Optional
    :param album: Optional
    :param page_size: Number of results to fetch
    :param page_number: Offset
    :return: List of tracks that match the above conditions
    """
    query = "select t.track_id, t.track_name, t.track_release_date, ar.artist_name, al.album_name, g.genre_name" \
            "  from Tracks t" \
            "  join Albums al on al.album_id = t.album_id and ({ALBUM_FILTER})" \
            "  join Genres g on g.genre_id = t.genre_id and ({GENRE_FILTER}) " \
            "  join Artists ar on ar.artist_id = t.artist_id " \
            " where ({DATE_FILTER})" \
            "   and ({TEXT_FILTER})" \
            " order by artist_name " \

    args = []
    text_filter, date_filter, album_filter, genre_filter = "1=1", "1=1", "1=1", "1=1"
    if album is not None:
        album_filter = "al.album_name = %s"
        args.append(album)

    if genre is not None:
        genre_filter = "g.genre_name = %s"
        args.append(genre)

    if from_date is not None and to_date is not None:
        date_filter = 'track_release date between %s and %s'
        args += [from_date, to_date]

    if search_text is not None:
        if by_lyrics:
            text_filter = "MATCH(track_lyrics) AGAINST (%s)"
            args.append(search_text)
        elif by_artist:
            text_filter = "artist_name like %s"
            args.append("%" + search_text + "%")
        else:
            text_filter = "track_name like %s"
            args.append("%" + search_text + "%")

    query = query.format(DATE_FILTER=date_filter,
                         ALBUM_FILTER=album_filter,
                         GENRE_FILTER=genre_filter,
                         TEXT_FILTER=text_filter)

    return query_to_json(query=query, args=tuple(args), page_size=page_size, page_number=page_number)
