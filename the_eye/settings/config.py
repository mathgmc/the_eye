import os
import logging
import sys

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# APP
app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# DB Config
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}/{}".format(
    os.getenv("DB_USER", "the_eye_app"),
    os.getenv("DB_PASSWORD", "theeye123"),
    os.getenv("DB_HOST", "db"),
    os.getenv("DB_NAME", "eye"),
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# LOGGING
logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s"
)
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
