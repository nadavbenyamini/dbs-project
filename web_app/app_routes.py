from flask import render_template
from flask import Blueprint
from web_app.app_logic import *

app_routes = Blueprint('app_routes', __name__)

"""
This file is for defining inputs and outputs of each route of the web_app itself
Internal logic, queries etc. are in other places
"""


@app_routes.route('/country/<country_id>')
def country_chart(country_id):
    tracks = get_tracks_by_country(country_id)
    country_name = tracks[0]['country_name']
    return render_template(template_name_or_list="country.html", tracks=tracks, country_name=country_name)


@app_routes.route('/show/<tab_name>/<limit>')
def show_table(tab_name, limit=100):
    rows = get_all_from_table(tab_name, limit)
    return render_template(template_name_or_list="base.html", rows=rows, title=tab_name)
