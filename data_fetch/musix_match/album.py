from data_fetch.musix_match.musix_match_api import MusixFetcher
from models.all_models import *


class AlbumPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'album.get'
        self.models = [Album()]

    def prepare_requests(self):
        album_ids = Track().get_distinct_values_by_field('album_id')
        requests = []
        for album_id in album_ids:
            requests.append({'album_id': album_id})
        return requests[:5]

    def response_to_items(self, request, response):
        assert 'message' in response and 'body' in response['message'] and 'album' in response['message']['body']
        item = response['message']['body']['album']
        item['album_release_date'] = item['updated_time']
        return [item]

