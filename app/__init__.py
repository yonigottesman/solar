from flask import Flask
from flask_bootstrap import Bootstrap
from apscheduler.schedulers.background import BackgroundScheduler
from . import nasa_daemon


app = Flask(__name__)
bootstrap = Bootstrap(app)
scheduler = BackgroundScheduler()
# scheduler.add_job(nasa_daemon.tick, 'interval', seconds=20)
scheduler.start()





from app import routes
