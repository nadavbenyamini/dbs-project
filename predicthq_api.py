from data_fetcher import fetch

ROOT_URL = 'https://api.predicthq.com/v1'
CLIENT_ID = 'QyBSpkW1WTs'
API_KEY = 'RaBuM5F73bGJzrNm4VHHkYepHN0m4vGbKP9co1PG_jGh2QdFy0ZqKg'
TOKEN = 'LjOqMPnQ_hBAZm7WYkK-2QasXV_2LMQjgRul___m'

headers = {"Authorization": "Bearer {}".format(TOKEN), "Accept": "application/json"}


def fetch_predicthq_internal(params):
    url = "{}/{}".format(ROOT_URL, params)
    return fetch(url, headers, params)
