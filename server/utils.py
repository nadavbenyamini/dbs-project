import traceback
from database import sql_executor
from flask import jsonify
import decimal

"""
General utilities supporting the different backend functions  
"""


def get_all_from_table(tab_name, limit):
    """
    Warning this function is for internal use only with a hardcoded value in tab_name to avoid SQL Injection
    :param tab_name: table in our DB
    :param limit: #rows
    :return: simple JSON of select * from tab_name
    """
    query = "select * from {} limit {}".format(tab_name, limit)
    db_results = sql_executor.select(query=query)
    return res_to_json(db_results)


def query_to_json(query, args=None, page_size=100000, page_number=1):
    try:
        db_results = sql_executor.select(query=query, args=args)
        return res_to_json(db_results, page_size=page_size, page_number=page_number)
    except sql_executor.NoResultsException as e:
        raise APIException(str(e), status_code=404)
    except Exception as e:
        raise APIException(str(e), status_code=500)


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


class APIException(Exception):
    """
    Customer error raising.
    For example wrong track id should be error 404 not 500
    """
    status_code = 400

    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        print('Message: {}\n{}'.format(message, traceback.format_exc()))
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_json(self):
        return jsonify({'message': self.message})

