import datetime
from peewee import Model, CharField, DateTimeField,ForeignKeyField
from database.models.product import Product
from database.database import db


class Provider(Model):
    name = CharField(255)
    registration_date = DateTimeField(default=datetime.datetime.now)



    class Meta:
        database = db

class ProductProvider(Model):  # Tabela intermediária para muitos-para-muitos
    product = ForeignKeyField(Product, backref='providers')
    provider = ForeignKeyField(Provider, backref='products')

    class Meta:
        database = db
