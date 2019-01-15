from flask import Flask
from flask_bootstrap import Bootstrap
from apscheduler.schedulers.background import BackgroundScheduler

def tick():
    print('Tick! The time is:')

app = Flask(__name__)
bootstrap = Bootstrap(app)
scheduler = BackgroundScheduler()
scheduler.add_job(tick, 'interval', seconds=3)
scheduler.start()





from app import routes
