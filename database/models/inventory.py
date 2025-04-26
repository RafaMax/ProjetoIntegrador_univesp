from peewee import Model, CharField, DateTimeField
from database.database import db
import datetime

class Inventory(Model):
    product_id = CharField()
    current_quantity = CharField()
    losses = CharField()
    entry = CharField()
    exit = CharField()
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
