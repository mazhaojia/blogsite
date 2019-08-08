from bson import ObjectId
from mongoengine import EmbeddedDocument, StringField, DateTimeField, LongField, ListField, EmbeddedDocumentField, ObjectIdField

from database.models.Reply import Reply


class Comment(EmbeddedDocument):
    oid = ObjectIdField(required=True, default=ObjectId, unique=True, primary_key=True)
    username = StringField(required=True)
    likes = LongField()
    dislikes = LongField()
    content = StringField(required=True)
    published_datetime: DateTimeField = DateTimeField(required=True)
    replies: ListField = ListField(EmbeddedDocumentField(Reply))
