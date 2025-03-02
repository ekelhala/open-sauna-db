from flask import Blueprint
from flask_restful import Api

from open_sauna_db.resources.saunas import (SaunaCollection,
                                            SaunaItem)

saunas_bp = Blueprint("saunas", __name__, url_prefix="/saunas")
saunas_api = Api(saunas_bp)

saunas_api.add_resource(SaunaCollection, "/")
saunas_api.add_resource(SaunaItem, "/<sauna:sauna>/")
