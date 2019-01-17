from flask import Flask
from flask_bootstrap import Bootstrap
from apscheduler.schedulers.background import BackgroundScheduler
from config import Config
from . import nasa_daemon
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
scheduler = BackgroundScheduler()
scheduler.add_job(nasa_daemon.tick, 'interval', seconds=60)
scheduler.start()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
