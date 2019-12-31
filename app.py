from flask import Flask
from flask import render_template
from flask import request

import sql_executor
import data_fetch.factory as fetcher_factory

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World\n'


@app.route('/all_artists')
def all_artists():
    query = "select * from artists"
    results = sql_executor.select(query=query)
    return str(results)



    # artists = [{'id': r[0], 'name': r[1]} for r in results['rows']]
    # return render_template(template_name_or_list="base.html", artists=artists)


@app.route('/get_artists')
def get_artists():
    params = request.args
    query = "select * from artists"
    args = {}
    if params and 'name' in params:
        query += " where name = %s"
        args = (params['name'], )

    results = sql_executor.select(query=query, args=args)
    artists = [{'id': r[0], 'name': r[1]} for r in results['rows']]
    return render_template(template_name_or_list="base.html", artists=artists)


@app.route('/test')
def test_template():
    return render_template(template_name_or_list='index.html', title="TEST")

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


# The only function in app.py that regards data fetching from remote APIs
# For example:
# http://127.0.0.1:5000/fetch/musix/chart.tracks.get?chart_name=top&page=1&page_size=5&country=us
# http://127.0.0.1:5000/fetch/predicthq/events?q=beyonce&country=us&categories=concerts&sort=country,-start
@app.route('/fetch/<source>/<path>')
def fetch_data(source, path):
    fetcher = fetcher_factory.build_fetcher(source)
    params = request.query_string.decode("utf-8")
    return fetcher.fetch(path, params)


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
