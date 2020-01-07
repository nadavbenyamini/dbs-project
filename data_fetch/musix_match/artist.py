from data_fetch.musix_match.musix_match_api import MusixFetcher
from models.all_models import *


class ArtistPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'artist.get'
        self.models = [Artist()]

    def prepare_requests(self):
        artist_ids = self.get_values_by_field(model=Track(), field='artist_id')
        requests = []
        for artist_id in artist_ids:
            requests.append({'artist_id': artist_id})
        return requests

    def response_to_items(self, request, response):
        assert 'message' in response and 'body' in response['message'] and 'artist' in response['message']['body']
        item = {k: v for k, v in response['message']['body']['artist'].items()}  # Clone
        item['artist_country_id'] = item['artist_country']
        return [item]

