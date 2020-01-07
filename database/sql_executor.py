import pymysql
from sshtunnel import SSHTunnelForwarder
import json


def select(query, args=tuple(), use_ssh=False):
    cursors = __execute(queries=[{'query': query, 'args': args}], use_ssh=use_ssh)
    cursor = cursors[0]
    try:
        res = {'headers': [], 'rows': []}
        for row in cursor:
            if len(res['headers']) == 0:
                res['headers'] = list(row.keys())
            res['rows'].append([row[k] for k in res['headers']])
        return res
    finally:
        cursor.close()


def insert(query, args=tuple(), use_ssh=False):
    cursors = __execute(queries=[{'query': query, 'args': args}], use_ssh=use_ssh)
    cursor = cursors[0]
    try:
        response = cursor.fetchall()
        return response
    except Exception as e:
        raise e
    finally:
        cursor.close()


def __execute(queries, use_ssh=False):
    """
    Private function, should be accessed by one of the functions above
    :param queries: list of dictionaries: [{'query': 'select...', 'args': {}}...]
    :param use_ssh: True iff connection should use ssh
    :return: list of cursors after cursor.execute
    """
    with open("./config/mysql_config.json") as mysql_conf_file:
        mysql_conf = json.load(mysql_conf_file)
        mysql_conf_file.close()

    if not use_ssh:
        return get_cursors(mysql_conf=mysql_conf,
                           port=mysql_conf['sql_port'],
                           queries=queries)

    with open("./config/ssh_config.json") as ssh_conf_file:
        ssh_conf = json.load(ssh_conf_file)
        ssh_host = ssh_conf['ssh_host']
        ssh_user = ssh_conf['ssh_user']
        ssh_password = ssh_conf['ssh_password']
        ssh_port = ssh_conf['ssh_port']
        ssh_conf_file.close()

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=(mysql_conf['sql_hostname'], mysql_conf['sql_port'])) as tunnel:
        return get_cursors(mysql_conf=mysql_conf,
                           port=tunnel.local_bind_port,
                           queries=queries)


def get_cursors(mysql_conf, port, queries):
    conn = pymysql.connect(host=mysql_conf['sql_hostname'],
                           user=mysql_conf['sql_username'],
                           passwd=mysql_conf['sql_password'],
                           db=mysql_conf['sql_main_database'],
                           port=port)

    cursors = []
    for query in queries:
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(query=query['query'], args=query['args'])
        conn.commit()
        cursors.append(cur)
    return cursors


# TODO: Delete this
"""
def insert_bulk(queries, use_ssh=False):
    final_queries = [{'query': q, 'args': tuple()} for q in queries]
    cursors = __execute(queries=final_queries, use_ssh=use_ssh)
    responses = []
    for cur in cursors:
        try:
            responses.append(cur.fetchone())
        except Exception as e:
            responses.append(str(e))
        finally:
            cur.close()
    return responses
"""
