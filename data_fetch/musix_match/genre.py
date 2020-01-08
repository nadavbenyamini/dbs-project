from data_fetch.musix_match.musix_match_api import MusixFetcher
from database.db_utils import *


class GenrePath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'music.genres.get'

    def prepare_requests(self):
        # Not much to do here, there are no params for this api path
        return [{}]

    def response_to_insert_queries(self, request, response):
        assert 'message' in response and 'body' in response['message'] and 'music_genre_list' in response['message']['body']
        query = "insert ignore into Genres (genre_id, genre_parent_id, genre_name) values "
        values = []
        for g in response['message']['body']['music_genre_list']:
            genre = g['music_genre']
            values.append("({}, {}, '{}')".format(genre['music_genre_id'],
                                                  genre['music_genre_parent_id'],
                                                  clean_string(genre['music_genre_name'])))

        query += ','.join(values)
        return [query]
