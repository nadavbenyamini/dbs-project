from flask import request, render_template
from flask import Blueprint
from database import sql_executor

main_routes = Blueprint('main', __name__)


@main_routes.route('/test')
def test_template():
    return render_template(template_name_or_list='index.html', title="TEST")


@main_routes.route('/all_artists')
def all_artists():
    query = "select * from artists"
    results = sql_executor.select(query=query)
    return str(results)


@main_routes.route('/get_artists')
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
