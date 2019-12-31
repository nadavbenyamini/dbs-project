from flask import Flask
from flask import render_template
from flask import request

import sql_executor
from musix_match_api import fetch_musix_internal
from predicthq_api import fetch_predicthq_internal

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World\n'


@app.route('/get_artists')
def get_artists():
    params = request.args
    query = "select * from artists"
    args = {}
    if params and 'name' in params:
        query = '{} {}'.format(query, "where name = %s")
        args = (params['name'], )

    results = sql_executor.select(query=query, args=args)
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


# For example:
# http://127.0.0.1:5000/musix?chart.tracks.get?chart_name=top&page=1&page_size=5&country=us
# http://127.0.0.1:5000/musix?chart.artists.get?chart_name=top&page=1&page_size=5&country=us
@app.route('/musix')
def fetch_musix():
    params = request.query_string.decode("utf-8")
    print(params)
    return fetch_musix_internal(params)


# For example:
# http://127.0.0.1:5000/predicthq?events?q=beyonce&country=us&categories=concerts&sort=country,-start
@app.route('/predicthq')
def fetch_predicthq():
    params = request.query_string.decode("utf-8")
    print(params)
    return fetch_predicthq_internal(params)


if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0", debug=True)
