from data_fetcher import fetch

ROOT_URL = 'https://api.musixmatch.com/ws/1.1'
API_KEY = 'c7692882e8a5eb99f12a16a6e176d2e2'
headers = {'Content-Type': 'application/json', 'apikey': API_KEY}


def fetch_musix_internal(params):
    url = '{}/{}&apikey={}'.format(ROOT_URL, params, API_KEY)
    return fetch(url)
