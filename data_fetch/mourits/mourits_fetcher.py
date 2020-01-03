from data_fetch.base_fetcher import BaseFetcher
from models.all_models import *


class MouritsFetcher(BaseFetcher):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://mourits.xyz:2096'
        self.headers = {'Content-Type': 'application/json'}
        self.path = ''
        self.models = [Lyrics()]

    def prepare_requests(self):
        tracks = Track().get_distinct_values_by_multiple_fields(['artist_id', 'track_name', 'track_id'])
        artists = Artist().get_distinct_values_by_multiple_fields(['artist_id', 'artist_name'])
        requests = []
        for t in tracks:
            for a in artists:
                if t[0] == a[0]:
                    requests.append({'a': a[1], 's': t[1], 'track_id': t[2], 'separator': '<br/>'})
        return requests

    def response_to_items(self, request, response):
        assert response['success']
        item = {
            'track_id': request['track_id'],
            'track_lyrics': response['result']['lyrics']
        }
        return [item]
