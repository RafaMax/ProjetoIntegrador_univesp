import datetime
from peewee import Model, DateTimeField, DecimalField, DateField
from database.database import db


class Buy(Model):
    date = DateField()
    quantity = DecimalField(11)
    product_id = DecimalField(11)
    provider_id = DecimalField(11)
    cost = DecimalField(10,2)
    user_id = DecimalField(11)
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db