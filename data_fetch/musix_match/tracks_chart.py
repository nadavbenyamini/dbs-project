from .musix_match_api import MusixFetcher
from models.all_models import *


class TracksChartPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'chart.tracks.get'
        self.models = [Track()]

    def prepare_requests(self):
        countries = Country().get_all_values_by_field('country_code')
        requests = []
        for country in countries:
            requests.append({'country': country})
        return requests

    def response_to_items(self, response):
        track_list = response['message']['body']['track_list']
        tracks = []
        for t in track_list:
            track = t['track']
            item = {k: v for k, v in track.items() if k != 'primary_genres'}  # Cloning
            genre_list = track.get('primary_genres', {}).get('music_genre_list', [])
            if len(genre_list) > 0:
                item['music_genre_id'] = genre_list[0]['music_genre']['music_genre_id']
            else:
                item['music_genre_id'] = None
            tracks.append(item)
        return tracks
