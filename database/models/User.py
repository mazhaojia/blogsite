from mongoengine import Document, StringField


class User(Document):
    phone = StringField(required=True, unique=True)
    username = StringField(required=True)
    password = StringField(required=True)
    picture_path = StringField()
