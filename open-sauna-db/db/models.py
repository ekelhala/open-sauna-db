from uuid import uuid4
from mongoengine import Document, GeoPointField, StringField

STOVE_TYPE = ('wood', 'electric')

class Sauna(Document):
    """
    A database model representing a sauna.
    """
    location = GeoPointField()
    name = StringField()
    sauna_id = StringField(primary_key=True, default=lambda: str(uuid4()))
    stove_type = StringField(choices=STOVE_TYPE)
