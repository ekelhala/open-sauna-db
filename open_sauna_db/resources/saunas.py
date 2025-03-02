"""
Resource definitions for sauna-related resources
"""
import json
from flask_restful import Resource
from flask import jsonify, request, Response
from jsonschema import validate, ValidationError
from werkzeug.exceptions import UnsupportedMediaType, BadRequest

from open_sauna_db.db.models import Sauna

class SaunaItem(Resource):
    """
    Resource for interacting with a single sauna
    """

    def get(self, sauna):
        """
        Get a single sauna
        """
        return jsonify(sauna.to_json())

    @staticmethod
    def json_schema():
        """
        Returns the JSON schema for this resource
        """
        return {
            "type": "object",
            "required": ["name", "location", "stove_type"],
            "properties": {
                "name": {"type": "string"},
                "location": {
                            "type": "object",
                            "properties": {
                                "latitude": {"type":"number"},
                                "longitude": {"type":"number"}
                            }
                            },
                "stove_type": {
                            "enum": ["wood", "electric"]
                }
            }
        }

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

    def post(self):
        """
        Create a new sauna
        """
        if not request.content_type == "application/json":
            raise UnsupportedMediaType
        try:
            validate(request.json, SaunaItem.json_schema())
            location = request.json["location"]
            new_sauna = Sauna(
                location = {
                    "type": "Point",
                    "coordinates": [location["longitude"], location["latitude"]]
                    },
                name=request.json["name"],
                stove_type=request.json["stove_type"]
            )
            new_sauna.save()
            return Response(
                json.dumps(new_sauna.to_json()),
                status=201
            )
        except ValidationError as validation_error:
            raise BadRequest(str(validation_error)) from validation_error
