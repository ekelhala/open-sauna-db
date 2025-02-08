from mongoengine import Document, GeoPointField, StringField, SequenceField

class Sauna(Document):
    """
    A database model representing a sauna.
    """
    location = GeoPointField()
    name = StringField()
    sauna_id = SequenceField()
