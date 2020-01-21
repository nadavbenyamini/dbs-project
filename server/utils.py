from database import sql_executor
from flask import jsonify, abort
import decimal

"""
General utilities supporting the different backend functions  
"""
ALL_TABLES = ['Charts', 'Countries', 'Tracks', 'TracksView', 'Genres', 'GenresView', 'Albums', 'Artist']


def get_all_from_table(tab_name, limit=10000000000, order_by=1):
    """
    Warning - this function formats query directly without using query args so it's exposed to injection
    Make sure the parameters are validated
    :param tab_name: table in our DB
    :param limit: #rows *NUMBER*
    :param order_by: order by column *NUMBER*
    :return: simple JSON of select * from tab_name
    """

    # Next 3 lines validate the parameters to prevent SQL injection
    assert tab_name in ALL_TABLES
    order_by = int(order_by)
    limit = int(limit)

    query = "select * from {} order by {} limit {}".format(tab_name, order_by, limit)
    db_results = sql_executor.select(query=query)
    return res_to_json(db_results)


def query_to_json(query, args=None, page_size=100000, page_number=1):
    try:
        db_results = sql_executor.select(query=query, args=args)
        return res_to_json(db_results, page_size=page_size, page_number=page_number)
    except sql_executor.NoResultsException:
        abort(404)
    except Exception as e:
        raise e


def res_to_json(res, page_size=100000, page_number=1):
    _rows = []
    headers = res['headers']
    first_res = (page_number - 1) * page_size
    last_res = page_number * page_size
    for row in res['rows'][first_res: last_res]:
        _rows.append({headers[i]: process_val(row[i]) for i in range(len(headers))})
    return jsonify(_rows)


# Fixing decimal issue in jsonify()
def process_val(val):
    return float(val) if isinstance(val, decimal.Decimal) else val
