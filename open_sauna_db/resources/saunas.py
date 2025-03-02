"""
Resource definitions for sauna-related resources
"""
from flask_restful import Resource
from flask import jsonify

from open_sauna_db.db.models import Sauna

class SaunaCollection(Resource):
    """
    Resource for interacting with all saunas
    """
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
    """
    Resource for interacting with a single sauna
    """

    def get(self, sauna):
        """
        Get a single sauna
        """
        return jsonify(sauna.to_json())
