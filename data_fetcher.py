import requests


def fetch(url, headers={}):
    response = requests.get(url, headers=headers)
    print(response.content)
    return response.content
