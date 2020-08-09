import mongoengine


class TwitterIntegration(mongoengine.EmbeddedDocument):
    status = mongoengine.BooleanField(default=False),
    tweet_roast_begin = mongoengine.BooleanField(default=False),
    tweet_roast_progress = mongoengine.BooleanField(default=False),
    tweet_roast_complete = mongoengine.BooleanField(default=False),
    consumer_key = mongoengine.StringField()
    consumer_secret = mongoengine.StringField()
    access_token_key = mongoengine.StringField()
    access_token_secret = mongoengine.StringField()