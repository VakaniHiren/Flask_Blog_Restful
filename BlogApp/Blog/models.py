from mongoengine import *
from itsdangerous import JSONWebSignatureSerializer as Serializer
import datetime

class User(Document):
    uname =  StringField(required=True)
    upass =  StringField(required=True)

class Blogpost(Document):
    refuser = ReferenceField(User,reverse_delete_rule=CASCADE)
    title = StringField()
    subtitle =  StringField()
    author =  StringField()
    date_posted = DateTimeField(default=datetime.datetime.now)
    content =  StringField()

class Followers(Document):
    followin = ReferenceField(User)
    follower =  ReferenceField(User)






