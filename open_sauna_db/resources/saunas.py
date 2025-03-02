from flask_restful import Resource
from flask import jsonify
from werkzeug.routing import BaseConverter
from werkzeug.exceptions import NotFound

from open_sauna_db.db.models import Sauna

class SaunaCollection(Resource):

    def get(self):
        """
        Get all saunas in database
        """
        # pylint: disable=no-member
        saunas = Sauna.objects()
        return jsonify(
            [sauna.to_json() for sauna in saunas]
        )

class SaunaItem(Resource):

    def get(self, sauna):
        """
        Get a single sauna
        """
        return jsonify(sauna.to_json())
