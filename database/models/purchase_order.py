import datetime

from peewee import Model, DateTimeField, DecimalField, DateField,ForeignKeyField
from database.models.product import Product
from database.models.provider import Provider
from database.database import db


class PurchaseOrder(Model):
    date = DateField()
    product = ForeignKeyField(Product, backref='purchase_order')
    provider = ForeignKeyField(Provider, backref='purchase_order')
    quantity = DecimalField(10, decimal_places=2)
    cost = DecimalField(10, decimal_places=2)
    
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db