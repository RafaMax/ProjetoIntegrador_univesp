import datetime
from peewee import Model, DateTimeField, DecimalField, CharField
from database.database import db


class Evaluation(Model):
    buy_id = DecimalField(11)
    ranking = CharField(255)
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db