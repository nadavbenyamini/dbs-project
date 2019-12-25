from flask import Flask
from flask import render_template
from flask import request

import sql_executor
from musix_match_api import fetch_musix

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World\n'


@app.route('/get_artists')
def get_artists():
    results = sql_executor.select("select * from artists")
    artists = [{'id': r[0], 'name': r[1]} for r in results['rows']]
    return render_template(template_name_or_list="base.html", artists=artists)


@app.route('/add_artist')
def post_artist():
    headers = ['id', 'name']
    params = request.args
    for h in headers:
        if h not in params:
            raise Exception('Invalid parameters. Must provide: {}'.format(str(headers)))
    query = "insert into artists select %(id)s, '%(name)s';"
    args = {'id': params['id'], 'name': params['name']}
    try:
        sql_executor.insert(query, args)
    except Exception as e:
        print('An error occurred: {}'.format(e))
    finally:
        return get_artists()


@app.route('/musix')
def fetch():
    params = request.query_string.decode("utf-8")
    print(params)
    return fetch_musix(params)


if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0", debug=True)
