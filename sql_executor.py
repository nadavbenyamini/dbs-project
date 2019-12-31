import pymysql
from sshtunnel import SSHTunnelForwarder
import json


def execute(query, args={}):
    with open("./config/mysql_config.json") as mysql_conf_file:
        mysql_conf = json.load(mysql_conf_file)
        print(mysql_conf)
        sql_hostname = mysql_conf['sql_hostname']
        sql_username = mysql_conf['sql_username']
        sql_password = mysql_conf['sql_password']
        sql_main_database = mysql_conf['sql_main_database']
        sql_port = mysql_conf['sql_port']

    with open("./config/ssh_config.json") as ssh_conf_file:
        ssh_conf = json.load(ssh_conf_file)
        print(ssh_conf)
        ssh_host = ssh_conf['ssh_host']
        ssh_user = ssh_conf['ssh_user']
        ssh_password = ssh_conf['ssh_password']
        ssh_port = ssh_conf['ssh_port']

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        db = pymysql.connect(host='127.0.0.1',
                             user=sql_username,
                             passwd=sql_password,
                             db=sql_main_database,
                             port=tunnel.local_bind_port)
        cur = db.cursor(pymysql.cursors.DictCursor)
        cur.execute(query, args=args)
        db.commit()
        db.close()
        ssh_conf_file.close()
        mysql_conf_file.close()
        return cur


def select(query, args={}):
    cursor = execute(query=query, args=args)
    try:
        res = {'headers': [], 'rows': []}
        for row in cursor:
            if len(res['headers']) == 0:
                res['headers'] = list(row.keys())
            res['rows'].append([row[k] for k in res['headers']])
        return res
    finally:
        cursor.close()


def insert(query, args):
    cursor = execute(query % args)  # TODO - change this line to prevent SQL Injection
    try:
        response = cursor.fetchone()
        print(response)
        return response
    except Exception as e:
        raise e
    finally:
        cursor.close()
