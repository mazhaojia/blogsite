from mongoengine import Document, StringField


class Category(Document):
    name = StringField(required=True, max_length=31)

