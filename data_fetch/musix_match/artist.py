from data_fetch.musix_match.musix_match_api import MusixFetcher


class ArtistPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'artist.get'

    def prepare_requests(self):
        artist_ids = [27840, 24748742]
        requests = []
        for artist_id in artist_ids:
            requests.append({'artist_id': artist_id})
        return requests

    def response_to_items(self, response):
        artist_json = response['message']['body']['artist']
        artist = {}
        for field in ['artist_id', 'artist_name', 'artist_country', 'artist_rating', 'updated_time']:
            artist[field] = artist_json.get(field, None)
        return [artist]

    def item_to_queries(self, item):
        query = 'insert into table artists select 1'
        args = {}
        return [(query, args)]
