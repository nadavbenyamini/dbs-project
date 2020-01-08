from data_fetch.musix_match.musix_match_api import MusixFetcher
from database.db_utils import *


class AlbumPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'album.get'

    def prepare_requests(self):
        query = "select distinct t.album_id " \
                "from Tracks t left join Albums a on a.album_id = t.album_id " \
                "where a.album_id is NULL"
        query_results = self.sql_executor.select(query)
        album_ids = [r[0] for r in query_results['rows']]
        requests = []
        for album_id in album_ids:
            requests.append({'album_id': album_id})
        return requests

    def response_to_insert_queries(self, request, response):
        assert 'message' in response and 'body' in response['message'] and 'album' in response['message']['body']
        album = response['message']['body']['album']
        release_date = validate_timestamp(album['updated_time'])
        query = "insert ignore into Albums (album_id, artist_id, album_name, album_rating, album_release_date)" \
                "values ({}, {}, '{}', {}, '{}')"\
            .format(album['album_id'],
                    album['artist_id'],
                    clean_string(album['album_name']),
                    album['album_rating'],
                    release_date if release_date is not None else 'NULL')

        return [query]
