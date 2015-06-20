__author__ = 'alisonbnt'

from flask import jsonify
from flask_restful import Resource

class IndexResource(Resource):

    @staticmethod
    def get():
        return jsonify({'hello': 'world'})
