import datetime

from peewee import Model, DateTimeField, DecimalField, DateField

from database.database import db


class PurchaseOrder(Model):
    date = DateField()
    product_id = DecimalField(11)
    quantity_ordered = DecimalField(11)
    user_id = DecimalField(11)
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db