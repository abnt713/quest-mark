__author__ = 'alisonbnt'

import flask
import conf.config as config

from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_cors import CORS
from flask_script import Manager, Server

app = flask.Flask(__name__)
cors = CORS(app)
api = Api(app)
db = config.load_db(app)
migrate = Migrate(app, db)

server = Server(host=config.APP_HOST, port=config.APP_PORT, use_debugger=config.APP_DEBUG)


manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', server)