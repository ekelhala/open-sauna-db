"""
Utility classes and functions
"""
from werkzeug.exceptions import NotFound
from werkzeug.routing import BaseConverter

from open_sauna_db.db.models import Sauna, Review

class SaunaConverter(BaseConverter):
    """
    URL converter for saunas
    """
    def to_python(self, value):
        # pylint: disable=no-member
        db_sauna = Sauna.objects(sauna_id=value).first()
        if db_sauna:
            return db_sauna
        raise NotFound(f"Sauna with id {value} does not exist.")

    def to_url(self, value):
        return str(value.sauna_id)

class ReviewConverter(BaseConverter):
    """
    URL converter for reviews
    """
    def to_python(self, value):
        # pylint: disable=no-member
        db_review = Review.objects(review_id=value)
        if db_review:
            return db_review
        raise NotFound(f"Review with id {value} does not exist.")

    def to_url(self, value):
        return str(value.review_id)