from uuid import uuid4
from mongoengine import Document, PointField, StringField, IntField, DateTimeField, EmailField

STOVE_TYPE = ('wood', 'electric')

class Sauna(Document):
    """
    A database model representing a sauna.
    """
    location = PointField()
    name = StringField()
    sauna_id = StringField(default=lambda: str(uuid4()))
    stove_type = StringField(choices=STOVE_TYPE)

    def to_json(self):
        """
        Returns this Sauna document as a Python dictionary
        """
        doc = {
            "location": {
                "longitude": self.location["coordinates"][0],
                "latitude": self.location["coordinates"][1]
            },
            "name": self.name,
            "sauna_id": self.sauna_id,
            "stove_type": self.stove_type
        }
        return doc

class Review(Document):
    review_id = StringField(default=lambda: str(uuid4()))
    for_sauna = StringField()
    by_user = StringField()
    text = StringField()
    stars = IntField()
    created_at = DateTimeField()

    def to_json(self):
        return {
            "review_id": self.review_id,
            "for_sauna": self.for_sauna,
            "by_user": self.by_user,
            "text": self.text,
            "stars": self.stars,
            "created_at": str(self.created_at)
        }

class User(Document):
    user_id = StringField(default=lambda: str(uuid4()))
    username = StringField(unique=True)
    password_hash = StringField()
    email = EmailField(unique=True)
