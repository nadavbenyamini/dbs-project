from .musix_match_api import MusixFetcher
from database.db_utils import *


class TracksChartPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'chart.tracks.get'

    def prepare_requests(self):
        page_count = 1
        page_size = 100
        first_country = 1
        last_country = 10  # pull countries [X:Y]

        query = "select distinct country_id, population from Countries order by population desc"
        query_results = self.sql_executor.select(query)
        all_countries = [r[0] for r in query_results['rows']]
        countries = all_countries[first_country: last_country]
        requests = []
        for country in countries:
            for p in range(1, page_count + 1):
                requests.append({'chart_name': 'top', 'country': country, 'page': p, 'page_size': page_size})
        return requests

    def response_to_insert_queries(self, request, response):
        chart_q = "insert ignore into Charts (country_id, track_id, track_rank) values "
        track_q = "insert ignore into Tracks " \
                  "(track_id, track_name, track_rating, genre_id, artist_id, album_id, track_release_date) values "
        chart_values = []
        track_values = []
        i = 0
        for t in response['message']['body']['track_list']:
            track = t['track']
            i += 1
            chart_values.append("('{}', {}, {})".format(request['country'], track['track_id'], i))
            release_date = validate_timestamp(track['updated_time'])

            genre_list = track.get('primary_genres', {}).get('music_genre_list', [])
            genre_id = None
            if len(genre_list) > 0:
                genre_id = genre_list[0]['music_genre']['music_genre_id']

            track_values.append("({}, '{}', {}, {}, {}, {}, '{}')".format(track['track_id'],
                                                                          clean_string(track['track_name']),
                                                                          track['track_rating'],
                                                                          genre_id if genre_id else 'NULL',
                                                                          track['artist_id'],
                                                                          track['album_id'],
                                                                          release_date if release_date else 'NULL'))

        queries = []
        if len(track_values) > 0:
            queries.append(track_q + ','.join(track_values))
        if len(chart_values) > 0:
            queries.append(chart_q + ','.join(chart_values))
        return queries

