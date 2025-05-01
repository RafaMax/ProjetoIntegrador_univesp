import datetime
from peewee import Model, CharField, DateTimeField
from database.database import db


class User(Model):
    name = CharField(255)
    e_mail = CharField(255)
    password = CharField(255)
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db