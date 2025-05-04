import datetime

from peewee import Model, DateTimeField, DecimalField

from database.database import db


class Inventory(Model):
    product_id = DecimalField(11)
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db