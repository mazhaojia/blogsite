from mongoengine import Document, StringField, ImageField


class User(Document):
    phone = StringField(required=True, max_length=31, primary_key=True)
    username = StringField(required=True, max_length=127)
    password = StringField(required=True, max_length=31)
    picture_path = StringField(required=True, max_length=511)
