from .musix_match_api import MusixFetcher


class TracksChartPath(MusixFetcher):
    def __init__(self):
        super().__init__()
        self.path = 'chart.tracks.get'

    def prepare_requests(self):
        countries = ['us', 'de']
        requests = []
        for country in countries:
            requests.append({'country': country})
        return requests

    def response_to_items(self, response):
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

    def item_to_records(self, item):
        table1 = 'tracks'
        record1 = tuple([item[f] for f in ['track_id', 'track_name', 'track_rating', 'updated_time']])

        table2 = 'artists'
        record2 = tuple([item[f] for f in ['artist_id', 'artist_name']])

        table3 = 'albums'
        record3 = tuple([item[f] for f in ['album_id', 'album_id']])
        return {table1: [record1],
                table2: [record2],
                table3: [record3]}
