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
        if len(res['headers']) == 0:
            raise Exception('Query returned 0 results: {}'.format(query))
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
        sql_hostname = mysql_conf['sql_hostname']
        sql_username = mysql_conf['sql_username']
        sql_password = mysql_conf['sql_password']
        sql_main_database = mysql_conf['sql_main_database']
        sql_port = mysql_conf['sql_port']

    with open("./config/ssh_config.json") as ssh_conf_file:
        ssh_conf = json.load(ssh_conf_file)
        ssh_host = ssh_conf['ssh_host']
        ssh_user = ssh_conf['ssh_user']
        ssh_password = ssh_conf['ssh_password']
        ssh_port = ssh_conf['ssh_port']

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        ssh_conf_file.close()
        mysql_conf_file.close()
        db = pymysql.connect(host='127.0.0.1',
                             user=sql_username,
                             passwd=sql_password,
                             db=sql_main_database,
                             port=tunnel.local_bind_port)

        cursors = []
        for query in queries:
            cur = db.cursor(pymysql.cursors.DictCursor)
            cur.execute(query=query['query'], args=query['args'])
            db.commit()
            cursors.append(cur)
    return cursors
