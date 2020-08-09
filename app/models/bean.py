import mongoengine as me


class Bean(me.Document):
    id = me.IntField()
    stock = me.IntField()
    label = me.StringField()
    origin = me.StringField()
    process = me.StringField()
    organic = me.BooleanField()
    fair_trade = me.BooleanField()
