from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime


class Product(Model):
    name = CharField()
    category = CharField()
    price = CharField()
    quality = CharField()
    seasonality = CharField()
    climate_id = CharField()
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
