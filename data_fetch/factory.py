from data_fetch.musix_match.tracks_chart import TracksChartPath
from data_fetch.musix_match.artist import ArtistPath


# The only interface with app.py
def start_fetching(source):
    fetchers = build_fetchers(source)
    summary = '\n'.join([f.fetch_all() for f in fetchers])
    return summary


# Factory function
def build_fetchers(source):
    if source == 'musix':
        return [TracksChartPath(), ArtistPath()]
    else:
        raise Exception('Invalid remote data source')

