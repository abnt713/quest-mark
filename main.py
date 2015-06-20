#!venv/bin/python
__author__ = 'alisonbento'

import app.routes as routes
from app import api, manager


routes.load_routes(api)

if __name__ == '__main__':
    manager.run()
