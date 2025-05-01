import datetime
from peewee import Model, CharField, DateTimeField
from database.database import db


class Provider(Model):
    name = CharField(255)
    contact = CharField(255)
    quality_assessed = CharField(100)
    product_type = CharField(255)
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db