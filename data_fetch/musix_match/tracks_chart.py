from .musix_match_api import MusixFetcher
from models.all_models import *


class TracksChartPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'chart.tracks.get'
        self.models = [Track(), Chart()]

    def prepare_requests(self):
        page_count = 10
        page_size = 100
        countries = self.get_values_by_field(model=Country(), field='country_id')
        requests = []
        for country in countries:
            for p in range(1, page_count + 1):
                requests.append({'chart_name': 'top', 'country': country, 'page': p, 'page_size': page_size})
        return requests

    def response_to_items(self, request, response):
        assert 'message' in response and 'body' in response['message'] and 'track_list' in response['message']['body']

        track_list = response['message']['body']['track_list']
        country_id = request['country']
        items = []
        i = 0
        for t in track_list:
            track = t['track']

            # Extracting Track properties
            item = {k: v for k, v in track.items() if k != 'primary_genres'}  # Cloning
            item['track_release_date'] = track['updated_time']
            genre_list = track.get('primary_genres', {}).get('music_genre_list', [])
            if len(genre_list) > 0:
                item['genre_id'] = genre_list[0]['music_genre']['music_genre_id']
            else:
                item['genre_id'] = None

            # Extracting Chart properties
            i += 1
            rank = (request['page'] - 1) * request['page_size'] + i
            item.update({'country_id': country_id, 'track_rank': rank})

            items.append(item)
        return items
