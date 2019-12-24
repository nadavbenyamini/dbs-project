from flask import Flask
import pymysql
app = Flask(__name__)


def test_query():
    db = pymysql.connect(user='DbMysql03', password='prodigy', host='mysqlsrv1.cs.tau.ac.il', database='DbMysql03')
    cur = db.cursor(pymysql.cursors.DictCursor)
    query = ("select * from artists")
    cur.execute(query)

    res = {}
    for row in cur:
	print('{}: {}'.format(row['id'], row['name']))
        res[row['id']] = row['name']

    db.close()
    return res


@app.route('/')
def hello_world():
    return test_query()
    # return 'Hello world'


if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0", debug=True)
