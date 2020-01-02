import data_fetch.factory as fetcher_factory
from flask import request
from flask import Blueprint

data_fetch_routes = Blueprint('data_fetch', __name__)


@data_fetch_routes.route('/fetch/<source>/<path>')
def fetch_data(source, path):
    """
    The main function for fetching, processing and inserting data from remote APIs into our DB
    :param source:
    :param path:
    :return: summary of fetching process from the relevant data fetcher
    """
    return fetcher_factory.fetch_remote_data(source, path)


# To test remote end points
@data_fetch_routes.route('/test/<source>/<path>')
def test_data(source, path):
    """
    For testing HTTP responses from remote APIs (only for sources mapped to our app, such as Musix).
    For example -
    http://127.0.0.1:5000/fetch/musix/chart.tracks.get?chart_name=top&page=1&page_size=5&country=us
    :param source:
    :param path:
    :return: HTTP Response
    """
    params = request.args
    return fetcher_factory.test_api_call(source, path, params)
