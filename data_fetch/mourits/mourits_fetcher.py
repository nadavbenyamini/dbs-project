from data_fetch.base_fetcher import BaseFetcher


class MouritsFetcher(BaseFetcher):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://mourits.xyz:2096'
        self.headers = {'Content-Type': 'application/json'}

    def response_to_items(self, response):
        return [response['message']['body']['artist']]
        pass
