import requests


ROOT_URL = 'https://api.musixmatch.com/ws/1.1/'


def fetch_data():
    url = 'chart.artists.get?page=1&page_size=10&country=us'
    full_url = '{}/{}'.format(ROOT_URL, url)
    response = requests.get(full_url)
    print(response.content)
