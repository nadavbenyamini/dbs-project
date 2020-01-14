from data_fetch.base_fetcher import BaseFetcher
from database.db_utils import *


class MouritsFetcher(BaseFetcher):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://mourits.xyz:2096'
        self.headers = {'Content-Type': 'application/json'}
        self.path = ''

    def prepare_requests(self):
        SIZE = 2
        query = "select distinct t.track_id, track_name, artist_name " \
                "from Tracks t join Artists a on t.artist_id = a.artist_id " \
                "left join Lyrics l on l.track_id = t.track_id where l.track_lyrics is NULL"
        rows = self.sql_executor.select(query)['rows']
        requests = []
        for row in rows[:SIZE]:
            requests.append({'track_id': row[0], 's': row[1], 'a': row[2], 'separator': '<br/>'})
        return requests

    # Inserting track_id to Lyrics table regardless of the response - if no lyrics found, insert NULL
    def response_to_insert_queries(self, request, response):
        print(response)
        if 'success' not in response or 'result' not in response or 'lyrics' not in response['result']:
            track_lyrics = '!'
        else:
            track_lyrics = clean_string(response['result']['lyrics'])
        query = "update Lyrics set track_lyrics = {} where track_id = {}".format(request['track_id'], track_lyrics)
        return [query]
