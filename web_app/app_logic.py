import traceback
from database import sql_executor
from flask import jsonify


def get_all_countries():
    return get_all_from_table('Countries', 10000)


def get_all_artists():
    return get_all_from_table('Artists', 10000)


def get_all_from_table(tab_name, limit):
    """
    An *UNSAFE* *TEMPORARY* method for testing
    # TODO - prevent SQL Injection (maybe make this a private method)
    :param tab_name: table in our DB
    :param limit: #rows
    :return: simple JSON of select * from tab_name
    """
    query = "select * from {} limit {}".format(tab_name, limit)
    db_results = sql_executor.select(query=query)
    return res_to_json(db_results)


# ------------------------------------------------------------------------------------------ #
# ---------------------------------  General Utilities ------------------------------------- #
# ------------------------------------------------------------------------------------------ #

def query_to_json(query, args=None):
    try:
        db_results = sql_executor.select(query=query, args=args)
        return res_to_json(db_results)
    except sql_executor.NoResultsException as e:
        raise APIException(str(e), status_code=404)
    except Exception as e:
        raise APIException(str(e), status_code=500)


def res_to_json(res):
    _rows = []
    headers = res['headers']
    for row in res['rows']:
        _rows.append({headers[i]: row[i] for i in range(len(headers))})
    return jsonify(_rows)


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

