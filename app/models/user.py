from werkzeug.security import check_password_hash
import mongoengine as me

from .integrations.twitter_integration import TwitterIntegration


class Integrations(me.EmbeddedDocument):
    twitter_bot = me.EmbeddedDocumentField(TwitterIntegration)


class User(me.Document):
    """User class used in the login process."""
    meta = dict(collection='accounts')
    username = me.StringField(required=True)
    password = me.StringField(required=True)
    email = me.StringField(required=True)
    first_name = me.StringField(required=True)
    last_name = me.StringField(required=True)
    integrations = me.EmbeddedDocumentField(Integrations)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def get_name(self):
        return self.first_name + " " + self.last_name

    def validate_login(self, input_password):
        return check_password_hash(self.password, input_password)
