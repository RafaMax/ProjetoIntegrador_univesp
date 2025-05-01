import datetime
from peewee import Model, DateField, DecimalField, CharField, DateTimeField
from database.database import db

class Climate(Model):
    date = DateField()
    temperature = DecimalField(5,2)
    product_impact = CharField(255)
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db