from flask import render_template
from flask import Blueprint
from web_app.app_logic import *

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
    return render_template(template_name_or_list="base.html", rows=rows, title=tab_name)