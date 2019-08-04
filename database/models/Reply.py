from mongoengine import EmbeddedDocument, StringField, LongField, DateTimeField


class Reply(EmbeddedDocument):
    username = StringField(required=True, max_length=31)
    likes = LongField()
    dislikes = LongField()
    content = StringField(required=True, max_length=1023)
    published_datetime = DateTimeField(required=True)
