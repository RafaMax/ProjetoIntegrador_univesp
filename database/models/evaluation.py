import datetime
from peewee import Model, DateTimeField, DecimalField, CharField,ForeignKeyField
from database.models.product import Product
from database.models.buy import Buy
from database.database import db


class Evaluation(Model):
    buy = ForeignKeyField(Buy, backref='evaluation')
    product = ForeignKeyField(Product, backref='evaluation')
    quantidade_avaliada = CharField(choices=['Pouca', 'Ideal', 'Muita'])
    qualidade_avaliada = CharField(choices=['Ruim', 'Bom', 'Top'])
    registration_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db