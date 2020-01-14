from flask import render_template
from flask import Blueprint
from database import sql_executor

app_routes = Blueprint('app_routes', __name__)


@app_routes.route('/country/<country_id>')
def country_chart(country_id):
    query = "select t.*, c.*, ch.track_rank " \
            "  from Countries c " \
            "  join Charts ch " \
            "    on c.country_id = ch.country_id" \
            "  join Tracks t" \
            "    on t.track_id = ch.track_id" \
            " where c.country_id = %s" \
            " order by track_rank"
    args = (country_id, )  # Converting to tuple...
    db_results = sql_executor.select(query=query, args=args)
    tracks = []
    headers = db_results['headers']
    for row in db_results['rows']:
        tracks.append({headers[i]: row[i] for i in range(len(headers))})
    country_name = tracks[0]['country_name']
    return render_template(template_name_or_list="country.html", tracks=tracks, country_name=country_name)


@app_routes.route('/show/<tab_name>/<limit>')
def show_table(tab_name, limit=100):
    query = "select * from {} limit {}".format(tab_name, limit)  # TODO - prevent SQL Injection
    db_results = sql_executor.select(query=query)
    rows = []
    headers = db_results['headers']
    for row in db_results['rows']:
        rows.append({headers[i]: row[i] for i in range(len(headers))})
    return render_template(template_name_or_list="base.html", rows=rows, title=tab_name)
