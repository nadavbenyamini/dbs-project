from flask import request, render_template
from flask import Blueprint
from database import sql_executor

main_routes = Blueprint('main', __name__)


@main_routes.route('/test')
def test_template():
    return render_template(template_name_or_list='index.html', title="TEST")


@main_routes.route('/show/<tab_name>')
def show_table(tab_name):
    params = request.args
    query = "select * from {}".format(tab_name)  # TODO - Fix to prevent SQL Injection
    args = {}
    if params and 'name' in params:
        query += " where name = %s"
        args = (params['name'], )

    db_results = sql_executor.select(query=query, args=args)
    rows = []
    headers = db_results['headers']
    for row in db_results['rows']:
        rows.append({headers[i]: row[i] for i in range(len(headers))})
    return render_template(template_name_or_list="base.html", rows=rows, title=tab_name)
