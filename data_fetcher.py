import requests


def fetch(url, headers={}, params={}):
    response = requests.get(url, headers=headers, params=params)
    print(response.content)
    return response.content
