from web_app.app_logic import *


def search_artist(search_text=""):
    """
    :param search_text: Text to search songs by
    :return: List of artists that contain search_text in their name
    """
    query = "select * from Artists a where artist_name like %s"
    args = tuple(['%'+search_text+'%'])
    return query_to_json(query, args)


def get_artists_by_country_id(country_id):
    """
    :param country_id:
    :return: artists: json of artists that had tracks in the country's chart
    """
    query = "select ar.artist_id, ar.artist_name," \
            "       c.country_id, c.country_name," \
            "       avg(ch.track_rank) as avg_track_rank " \
            "  from Countries c " \
            "  join Charts ch " \
            "    on c.country_id = ch.country_id " \
            "  join Tracks t" \
            "    on t.track_id = ch.track_id " \
            "  join Artists ar " \
            "    on ar.artist_id = t.artist_id " \
            " where c.country_id = %s" \
            " group by 1, 2, 3, 4" \
            " order by avg_track_rank"
    args = (country_id, )  # Converting to tuple...
    return query_to_json(query, args)


def get_artist_by_id(artist_id):
    query = "select * from Artists a where artist_id = %s"
    args = int(artist_id)
    return query_to_json(query, args)
