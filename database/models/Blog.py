from mongoengine import Document, ReferenceField, StringField, LongField, DateTimeField, ListField, EmbeddedDocumentField

from database.models.Category import Category
from database.models.Comment import Comment


class Blog(Document):
    category = ReferenceField(Category, required=True)
    title = StringField(required=True, max_length=127)
    likes = LongField()
    dislikes = LongField()
    viewed_numbers = LongField()
    content = StringField(required=True)
    published_dateTime = DateTimeField(required=True)
    last_modified_dateTime = DateTimeField()
    tags = ListField(StringField(max_length=31))
    comments = ListField(EmbeddedDocumentField(Comment))
