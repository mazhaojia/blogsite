from mongoengine import Document, ReferenceField, StringField, LongField, DateTimeField, ListField, EmbeddedDocumentField

from database.models.Category import Category
from database.models.Comment import Comment


class Blog(Document):
    category = ReferenceField(Category, required=True)
    title = StringField(required=True)
    likes = LongField()
    dislikes = LongField()
    viewed_numbers = LongField()
    content = StringField(required=True)
    published_dateTime = DateTimeField(required=True)
    last_modified_dateTime = DateTimeField()
    tags = ListField(StringField())
    comments = ListField(EmbeddedDocumentField(Comment))
