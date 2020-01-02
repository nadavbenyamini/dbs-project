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
        return requests

    def response_to_items(self, request, response):
        return [response['message']['body']['album']]

