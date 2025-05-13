import datetime
from peewee import Model, CharField, DateTimeField, DecimalField
from database.database import db

class Product(Model):
    name = CharField(255)
    category = CharField(100)
    price = DecimalField(10,2)
    quality = CharField(100)
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
       