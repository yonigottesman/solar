from app import app
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    status = 1234
    return render_template('index.html', status=status)
