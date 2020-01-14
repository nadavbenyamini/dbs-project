from flask import render_template
from flask import Blueprint
from web_app.app_logic import *
from config import *

app_routes = Blueprint('app_routes', __name__)

"""
This file is for defining inputs and outputs of each route of the web_app itself
Internal logic, queries etc. are in other places
"""


@app_routes.route('/countries')
def all_countries():
    return get_all_countries()


@app_routes.route('/country_tracks/<country_id>')
def country_tracks(country_id):
    return get_tracks_by_country(country_id)


@app_routes.route('/artist_tracks/<artist_id>')
def artist_tracks(artist_id):
    return get_tracks_by_artist(artist_id)


@app_routes.route('/show/<tab_name>/<limit>')
def show_table(tab_name, limit=100):
    rows = get_all_from_table(tab_name, limit)
    return render_template(template_name_or_list="old/base.html", rows=rows, title=tab_name)


@app_routes.route('/test')
def temp():
    return render_template(template_name_or_list="charts_albums.html", base_url=BASE_URL)

"""
    <script>
    function launch() {
        const base_url = '{{ base_url }}';
            fetch('http://' + base_url + '/country_tracks/us').then(res => res.json())
                .then(res => build_table(res['results']))
                .catch(e => console.log(e));
        }

    function build_table(rows) {
        const table = document.getElementById('gable');
        for(const row of rows) {
            const tr = document.createElement('tr');
            console.log(row);
            tr.innerHTML = '<td>' + row['track_name'] + '</td>' +
            '<td>' + row.track_id + '</td>' +
            '<td>' + row.country_id + '</td>' +
            '<td>' + row.rank + '</td>';
            $(table).append(tr);
        }
    }
    </script>
"""