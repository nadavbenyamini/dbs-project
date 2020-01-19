from server.utils import *
from flask import Blueprint

genre_routes = Blueprint('genre_routes', __name__)


@genre_routes.route('/api/genres', methods=['GET'])
def get_artist():
    return get_all_from_table('GenresView')
    ''' TODO - DELETE THIS:
    query = " select g1.genre_id, "\
            "        case when g2.genre_id=34 or g2.genre_id is NULL "\
            "             then g1.genre_name "\
            "             else concat(g2.genre_name, '/', g1.genre_name) end as genre_full_name "\
            "  from Genres g1 "\
            "  left join Genres g2 on g1.genre_parent_id = g2.genre_id "\
            " where g2.genre_id is null or g1.genre_id != 34 /*34='Music' the root genre*/ " \
            " order by genre_full_name "
    return query_to_json(query)
    '''

