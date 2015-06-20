__author__ = 'alisonbnt'

# CONFIG SAMPLE
# -------------
# Copy this file and rename it as "config.py"
# Fill the desired variables with your respective configuration settings

from flask_sqlalchemy import SQLAlchemy

APP_HOST = '0.0.0.0'
APP_PORT = 8080
APP_DEBUG = True
APP_DB_URI = 'mysql://username:password@host/db'
APP_SECRET_KEY = 'Some Secret Key'


def load_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = APP_DB_URI
    return SQLAlchemy(app)