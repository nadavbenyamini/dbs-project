from data_fetch.musix_match.musix_match_api import MusixFetcher
from models.all_models import *


class GenrePath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'music-genres-get'
        self.models = [Genre()]

    def prepare_requests(self):
        # Not much to do here, there are no params for this api path
        return [{}]

    def response_to_items(self, response):
        items = []
        for g in response['message']['body']['music_genre_list']:
            genre = g['music_genre']
            items.append({k.replace('music_', ''): v for k, v in genre.items()})
        return items

