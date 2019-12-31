from data_fetch.base_fetcher import BaseFetcher
API_KEY = 'c7692882e8a5eb99f12a16a6e176d2e2'


class MusixFetcher(BaseFetcher):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://api.musixmatch.com/ws/1.1'
        self.headers = {'Content-Type': 'application/json'}

    # Overriding because of api_key
    def get_url(self):
        return '{}/{}?apikey={}'.format(self.base_url, self.path, API_KEY)

    def process_response(self, response):
        pass
