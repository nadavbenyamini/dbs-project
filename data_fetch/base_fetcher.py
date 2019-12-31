import requests


# Base class
class BaseFetcher:
    def __init__(self):
        self.base_url = ''
        self.headers = {}

    def get_url(self, path):
        return '{}/{}'.format(self.base_url, path)

    def fetch(self, path, params={}):
        url = self.get_url(path)
        print('Fetching from {}, params={}'.format(url, params))
        response = requests.get(url=url, headers=self.headers, params=params)
        return response.content
