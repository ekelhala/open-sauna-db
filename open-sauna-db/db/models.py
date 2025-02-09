from uuid import uuid4
from mongoengine import Document, PointField, StringField

STOVE_TYPE = ('wood', 'electric')

class Sauna(Document):
    """
    A database model representing a sauna.
    """
    location = PointField()
    name = StringField()
    sauna_id = StringField(default=lambda: str(uuid4()))
    stove_type = StringField(choices=STOVE_TYPE)

    def to_dict(self):
        """
        Returns this Sauna document as a Python dictionary
        """
        data = self.to_mongo().to_dict()
        print(data)
        coordinates = data["location"]["coordinates"]
        data["location"] = {"longitude": coordinates[0], "latitude": coordinates[1]}
        return data
