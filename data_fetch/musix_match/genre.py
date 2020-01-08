from data_fetch.musix_match.musix_match_api import MusixFetcher
from models.all_models import *


class GenrePath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'music.genres.get'
        self.models = [Genre()]

    def prepare_requests(self):
        # Not much to do here, there are no params for this api path
        return [{}]

    def response_to_items(self, request, response):
        assert 'message' in response and 'body' in response['message'] and 'music_genre_list' in response['message']['body']
        items = []
        for g in response['message']['body']['music_genre_list']:
            genre = g['music_genre']
            items.append({k.replace('music_', ''): v for k, v in genre.items()})
        return items

    def response_to_insert_queries(self, request, response):
        assert 'message' in response and 'body' in response['message'] and 'music_genre_list' in response['message']['body']
        query = "insert ignore into Genres (genre_id, genre_parent_id, genre_name) values {}"
        values = []
        for item in response['message']['body']['music_genre_list']:
            values += "({}, {}, {}, {})".format(item['music_genre_id'], item['music_genre_parent_id'], item['music_genre_name'])

        query = query.format(','.join(values))
        return [query]
