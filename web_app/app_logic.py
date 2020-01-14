from database import sql_executor


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
    db_results = sql_executor.select(query=query, args=args)
    tracks = []
    headers = db_results['headers']
    for row in db_results['rows']:
        tracks.append({headers[i]: row[i] for i in range(len(headers))})
    return tracks


def get_all_from_table(tab_name, limit):
    """
    An *UNSAFE* *TEMPORARY* method for testing
    :param tab_name: table in our DB
    :param limit: #rows
    :return: simple JSON of select * from tab_name
    """
    query = "select * from {} limit {}".format(tab_name, limit)  # TODO - prevent SQL Injection
    db_results = sql_executor.select(query=query)
    rows = []
    headers = db_results['headers']
    for row in db_results['rows']:
        rows.append({headers[i]: row[i] for i in range(len(headers))})