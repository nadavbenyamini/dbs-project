from data_fetch.musix_match.tracks_chart import TracksChartPath
from data_fetch.musix_match.artist import ArtistPath
from data_fetch.musix_match.genre import GenrePath
from data_fetch.musix_match.album import AlbumPath
from data_fetch.mourits.mourits_fetcher import MouritsFetcher
from data_fetch.musix_match.track import TracksPath


def test_api_call(source, path, params):
    """
    :param source: data source, i.e. musix
    :param path: specific API path
    :param params: HTTP query params
    :return: HTTP Response
    """
    fetcher = build_fetchers(source, path)
    return fetcher.fetch(params).json()


def fetch_remote_data(source, path):
    """
    Builds the relevant data fetcher class and calls that class to start fetching data
    :param source: remote data source, i.e. musix, wikipedia etc.
    :param path: specific API path, i.e. artist.get
    :return: JSON summary of the fetching process
    """
    fetcher = build_fetchers(source, path)
    return fetcher.fetch_all()


# Factory function to find the relevant class per path and source
def build_fetchers(source, path):
    fetchers = {
        'musix': {
            'chart.tracks.get': TracksChartPath(),
            'artist.get': ArtistPath(),
            'album.get': AlbumPath(),
            'music.genres.get': GenrePath(),
            'tracks.get': TracksPath()
        },
        'mourits': {
            'lyrics': MouritsFetcher()
        }
    }
    try:
        return fetchers[source][path]
    except KeyError:
        raise Exception('Invalid remote data source or path')

