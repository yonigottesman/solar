from app import app
from app.models import Body, Delta
from flask import render_template, flash, redirect, url_for
from datetime import datetime, timedelta


@app.route('/')
@app.route('/index')
def index():
    
    body = choose_random_body()
    
    deltas = body.deltas.filter(Delta.time >= datetime.utcnow())\
                        .order_by(Delta.time.asc())[0:60]

    status = deltas[0].au*149597870700/1000
    
    return render_template('index.html',
                           body=body,
                           status="{0:.2f}".format(status),
                           deltas=[{'time': d.time.strftime("%Y-%b-%d %H:%M"),
                                    'delta': "{0:.2f}".format(d.au*149597870700 / 1000)}
                                   for d in deltas])


def choose_random_body():
    body = Body.query.filter_by(name='Mars').all()[0]
    return body

