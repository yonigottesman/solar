from app import app
from app.models import Body, Delta
from flask import render_template, flash, redirect, url_for
from datetime import datetime, timedelta
from flask import send_from_directory
import os
@app.route('/')
@app.route('/index')
def index():

    body = choose_random_body()

    deltas = body.deltas\
                 .filter(Delta.time >= datetime.utcnow()-timedelta(minutes=2))\
                 .order_by(Delta.time.asc())[0:60]

    return render_template('index.html',
                           body=body,
                           deltas=[{'time': d.time.strftime("%Y-%-m-%d %-H:%-M"),
                                    'au': "{0:.2f}".format(d.au*149597870700 / 1000)}
                                   for d in deltas])


def choose_random_body():
    body = Body.query.filter_by(name='Mars').all()[0]
    return body


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
