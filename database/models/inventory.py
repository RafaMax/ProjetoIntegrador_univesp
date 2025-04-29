import datetime
from peewee import Model, DateTimeField, DecimalField, DateField
from database.database import db

class Inventory(Model):
    product_id = DecimalField(11)
    current_quantity = DecimalField(11)
    losses = DecimalField(11)
    entry = DateField()
    exit = DateField()
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db