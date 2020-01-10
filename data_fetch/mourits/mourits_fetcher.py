from data_fetch.base_fetcher import BaseFetcher
from database.db_utils import *


class MouritsFetcher(BaseFetcher):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://mourits.xyz:2096'
        self.headers = {'Content-Type': 'application/json'}
        self.path = ''

    def prepare_requests(self):
        SIZE = 1
        query = "select distinct t.track_id, track_name, artist_name " \
                "from Tracks t join Artists a on t.artist_id = a.artist_id " \
                "left join Lyrics l on l.track_id = t.track_id where l.track_id is NULL"
        rows = self.sql_executor.select(query)['rows']
        requests = []
        for row in rows[:SIZE]:
            requests.append({'track_id': row[0], 's': row[1], 'a': row[2], 'separator': '<br/>'})
        return requests

    def response_to_insert_queries(self, request, response):
        assert response['success']
        query = "insert ignore into Lyrics (track_id, track_lyrics) values ({}, '{}')"\
            .format(request['track_id'],
                    clean_string(response['result']['lyrics']))
        return [query]
