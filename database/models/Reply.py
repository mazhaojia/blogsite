from bson import ObjectId
from mongoengine import EmbeddedDocument, StringField, LongField, DateTimeField, ObjectIdField


class Reply(EmbeddedDocument):
    oid = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    username = StringField(required=True)
    likes = LongField()
    dislikes = LongField()
    content = StringField(required=True)
    published_datetime = DateTimeField(required=True)
