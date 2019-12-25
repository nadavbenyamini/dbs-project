from flask import Flask
from flask import render_template
from flask import request
import pymysql

from musix_match_api import fetch_musix

app = Flask(__name__)


def test_query():
    db = pymysql.connect(user='DbMysql03', password='prodigy', host='mysqlsrv1.cs.tau.ac.il', database='DbMysql03')
    cur = db.cursor(pymysql.cursors.DictCursor)
    query = ("select * from artists")
    cur.execute(query)

    res = {}
    for row in cur:
        print(row)
        res[row['id']] = row['name']

    db.close()
    return res


@app.route('/')
def hello_world():
    return 'Hello World\n'


@app.route('/artists')
def get_artists():
    artists_json = test_query()
    print(str(artists_json))
    artists = [{'id': key, 'name': value} for key, value in artists_json.items()]
    return str(artists)


@app.route('/musix')
def fetch():
    params = request.query_string.decode("utf-8")
    print(params)
    return fetch_musix(params)


if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0", debug=True)
