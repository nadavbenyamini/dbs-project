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
        query = "select distinct t.track_id, track_name, artist_name " \
                "from Tracks t join Artists a on t.artist_id = a.artist_id " \
                "left join Lyrics l on l.track_id = t.track_id where l.track_id is NULL"
        rows = self.sql_executor.select(query)['rows']
        requests = []
        for row in rows:
            requests.append({'track_id': row[0], 's': row[1], 'a': row[2], 'separator': '<br/>'})
        return requests

    def response_to_items(self, request, response):
        assert response['success']
        item = {
            'track_id': request['track_id'],
            'track_lyrics': response['result']['lyrics']
        }
        return [item]
