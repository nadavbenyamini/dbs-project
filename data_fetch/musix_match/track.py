from data_fetch.musix_match.musix_match_api import MusixFetcher
from database.db_utils import *


class TracksPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'track.get'

    def prepare_requests(self):
        query = "select distinct c.track_id " \
                "from Charts c left join Tracks t on c.track_id = t.track_id " \
                "where t.track_id is NULL"
        query_results = self.sql_executor.select(query)
        track_ids = [r[0] for r in query_results['rows']]
        requests = []
        for track_id in track_ids:
            requests.append({'track_id': track_id})
        return requests

    def response_to_insert_queries(self, request, response):
        track_q = "insert ignore into Tracks " \
                  "(track_id, track_name, track_rating, genre_id, artist_id, album_id, track_release_date) values "
        track_values = []
        assert 'message' in response and 'body' in response['message'] and 'track' in response['message']['body']
        track = response['message']['body']['track']
        release_date = validate_timestamp(track['updated_time'])

        genre_list = track.get('primary_genres', {}).get('music_genre_list', [])
        genre_id = None
        if len(genre_list) > 0:
            genre_id = genre_list[0]['music_genre']['music_genre_id']

        track_values.append("({}, '{}', {}, {}, {}, {}, '{}')".format(request['track_id'],
                                                                      clean_string(track['track_name']),
                                                                      track['track_rating'],
                                                                      genre_id if genre_id else 'NULL',
                                                                      track['artist_id'],
                                                                      track['album_id'],
                                                                      release_date if release_date else 'NULL'))

        queries = []
        if len(track_values) > 0:
            queries.append(track_q + ','.join(track_values))
        return queries

