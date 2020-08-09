import mongoengine as me
from .roast import Roast
from .user import User


class Brew(me.Document):
    user = me.ReferenceField(User)
    roast = me.ReferenceField(Roast)
    datetime = me.DateTimeField()
    input_weight = me.IntField()
    output_weight = me.IntField()
    brew_time = me.IntField()
    brew_method = me.StringField()
    tags = me.ListField(me.StringField())
    wet_smell = me.ListField(me.StringField())
    dry_smell = me.ListField(me.StringField())
    grind_smell = me.ListField(me.StringField())
    tasting_notes = me.StringField()
