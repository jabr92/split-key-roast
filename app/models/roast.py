import mongoengine as me

from .bean import Bean
from .user import User


class RoastDataPoint(me.EmbeddedDocument):
    bean_temp = me.FloatField()
    environment_temp = me.FloatField()
    chaff_tray = me.BooleanField()
    cooling_motor = me.BooleanField()
    drum_motor = me.BooleanField()
    solenoid = me.BooleanField()
    fan = me.IntField()
    heater = me.IntField()
    main_fan = me.IntField()
    time = me.FloatField()
    valid = me.BooleanField()


class Roast(me.Document):
    name = me.StringField()
    coffee = me.ReferenceField(Bean)
    user = me.ReferenceField(User)
    input_weight = me.FloatField()
    duration = me.IntField()
    rest_days = me.IntField()
    date = me.DateField()
    events = me.ListField()
