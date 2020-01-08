from data_fetch.musix_match.musix_match_api import MusixFetcher
from database.db_utils import *


class ArtistPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'artist.get'

    def prepare_requests(self):
        query = "select distinct t.artist_id " \
                "from Tracks t left join Artists a on a.artist_id = t.artist_id " \
                "where a.artist_id is NULL"
        query_results = self.sql_executor.select(query)
        artist_ids = [r[0] for r in query_results['rows']]
        requests = []
        for artist_id in artist_ids:
            requests.append({'artist_id': artist_id})
        return requests

    def response_to_insert_queries(self, request, response):
        assert 'message' in response and 'body' in response['message'] and 'artist' in response['message']['body']
        artist = response['message']['body']['artist']
        query = "insert ignore into Artists (artist_id, artist_name, artist_country_id, artist_rating)" \
                "values ({}, '{}', '{}', {})"\
            .format(artist['artist_id'],
                    clean_string(artist['artist_name']),
                    artist['artist_country'],
                    artist['artist_rating'])

        return [query]
