from .musix_match_api import MusixFetcher


class TracksChartPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'chart.tracks.get'

    def prepare_requests(self):
        countries = ['us', 'de']
        self.requests = []
        for country in countries:
            self.requests.append({'country': country})

    def process_response(self, response):
        track_list = response['message']['body']['track_list']
        tracks = []
        for t in track_list:
            item = {}
            for field in ['track_id', 'track_name', 'album_id', 'album_name', 'artist_id',
                          'artist_name', 'track_rating', 'updated_time']:
                item[field] = t['track'].get(field, None)
                genre_list = t['track'].get('primary_genres', {}).get('music_genre_list', [])
                if len(genre_list) > 0:
                    item['music_genre_id'] = genre_list[0]['music_genre']['music_genre_id']
                else:
                    item['music_genre_id'] = None

            tracks.append(item)
        return tracks

