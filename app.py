from flask import Flask
from flask import render_template
from routes.data_fetch_routes import data_fetch_routes
from routes.app_routes import app_routes

app = Flask(__name__)
app.register_blueprint(data_fetch_routes)
app.register_blueprint(app_routes)

HOST = '0.0.0.0'
PORT = 5001


@app.route('/country')
def country_page():
    return render_template(template_name_or_list="country.html", base_url=HOST+':'+str(PORT))


@app.route('/')
def hello_world():
    return 'Hello World\n'


if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=True)
