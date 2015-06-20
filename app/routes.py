__author__ = 'alisonbnt'

from app.resources.api.index_resource import *

def load_routes(api):
    api.add_resource(IndexResource, '/api')
