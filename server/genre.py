from server.utils import *
from flask import Blueprint

genre_routes = Blueprint('genre_routes', __name__)


@genre_routes.route('/api/genres', methods=['GET'])
def get_genres():
    return get_all_from_table('GenresView', order_by=3)

