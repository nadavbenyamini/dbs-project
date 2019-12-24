from flask import Flask
import pymysql
app = Flask(__name__)

"""
def test_query():
    cnx = pymysql.connect(user='DbMysql03', password='prodigy', host='mysqlsrv1.cs.tau.ac.il', database='DbMysql03')
    cursor = cnx.cursor
    query = ("select * from artists")
    cursor.execute(query)

    res = {}
    for (id, name) in cursor:
        res[id] = name

    cnx.close()
    return res
"""

@app.route('/')
def hello_world():
    # return test_query()
    return 'Hello world'


if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0", debug=True)
