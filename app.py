from flask import Flask
from flask import render_template

import pymysql
app = Flask(__name__)


def test_query():
    db = pymysql.connect(user='DbMysql03', password='prodigy', host='mysqlsrv1.cs.tau.ac.il', database='DbMysql03')
    cur = db.cursor(pymysql.cursors.DictCursor)
    query = ("select * from artists")
    cur.execute(query)

    res = {}
    for (id, name) in cur:
        res[id] = name

    db.close()
    return res


@app.route('/')
def hello_world():
    artists_json = test_query()
    artists = [{'id': key, 'name': value} for key, value in artists_json.items()]
    return render_template('base.html', artists=artists)


if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0", debug=True)
