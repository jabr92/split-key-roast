import mongoengine as me
from .user import User

class Bean(me.Document):
    meta = dict(collection='inventory')
    user = me.ReferenceField(User)
    label = me.StringField()
    origin = me.StringField()
    process = me.StringField()
    stock = me.IntField()
    organic = me.BooleanField()
    fair_trade = me.BooleanField()
    tags = me.ListField(me.StringField())
    datetime = me.DateTimeField()

