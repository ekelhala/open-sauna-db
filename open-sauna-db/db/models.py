from mongoengine import Document, GeoPointField, StringField, SequenceField

STOVE_TYPE = ('wood', 'electric')

class Sauna(Document):
    """
    A database model representing a sauna.
    """
    location = GeoPointField()
    name = StringField()
    sauna_id = SequenceField()
    stove_type = StringField(choices=STOVE_TYPE)
