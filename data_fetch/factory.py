from data_fetch.predicthq_api import PredicthqFetcher
from data_fetch.musix_match_api import MusixFetcher


# Factory function
def build_fetcher(source):
    if source == 'musix':
        return MusixFetcher()
    elif source == 'predicthq':
        return PredicthqFetcher
    return None

