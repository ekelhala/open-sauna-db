"""
This is the main module for the API
"""
from flask import Flask

from open_sauna_db.db import driver
from open_sauna_db.saunas import saunas_bp

from open_sauna_db.utils import (SaunaConverter)

app = Flask(__name__)
driver.init()

#registering converters
app.url_map.converters["sauna"] = SaunaConverter

app.register_blueprint(saunas_bp)
