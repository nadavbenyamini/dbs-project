from server.utils import *
from flask import Blueprint

genre_routes = Blueprint('genre_routes', __name__)


@genre_routes.route('/api/genres', methods=['GET'])
def get_artist():
    return get_all_from_table('Genres', 10000000)
