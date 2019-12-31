from data_fetch.base_fetcher import BaseFetcher

CLIENT_ID = 'QyBSpkW1WTs'
API_KEY = 'RaBuM5F73bGJzrNm4VHHkYepHN0m4vGbKP9co1PG_jGh2QdFy0ZqKg'
TOKEN = 'LjOqMPnQ_hBAZm7WYkK-2QasXV_2LMQjgRul___m'


class PredicthqFetcher(BaseFetcher):
    def __init__(self):
        self.base_url = 'https://api.predicthq.com/v1'
        self.headers = {"Authorization": "Bearer {}".format(TOKEN), "Accept": "application/json"}

