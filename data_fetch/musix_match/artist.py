from data_fetch.musix_match.musix_match_api import MusixFetcher
from models.all_models import *


class ArtistPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'artist.get'
        self.models = [Artist()]

    def prepare_requests(self):
        artist_ids = Track().get_all_values_by_field('artist_id')
        requests = []
        for artist_id in artist_ids:
            requests.append({'artist_id': artist_id})
        return requests

    def response_to_items(self, response):
        return [response['message']['body']['artist']]

