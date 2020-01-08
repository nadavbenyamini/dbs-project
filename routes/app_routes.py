from flask import render_template
from flask import Blueprint
from database import sql_executor

app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/show/<tab_name>/<limit>')
def show_table(tab_name, limit=100):
    query = "select * from {} limit {}".format(tab_name, limit)  # TODO - prevent SQL Injection
    db_results = sql_executor.select(query=query)
    rows = []
    headers = db_results['headers']
    for row in db_results['rows']:
        rows.append({headers[i]: row[i] for i in range(len(headers))})
    return render_template(template_name_or_list="base.html", rows=rows, title=tab_name)
