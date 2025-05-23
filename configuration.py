from database.database import db
from database.models.buy import Buy
from database.models.evaluation import Evaluation
from database.models.inventory import Inventory
from database.models.product import Product
from database.models.provider import Provider, ProductProvider
from routes.buy import buy_route
from routes.evaluation import evaluation_route
from routes.home import home_route
from routes.inventory import inventory_route
from routes.product import product_route
from routes.provider import provider_route

from routes.avaliacao import avaliacao_route
from routes.gestaof import gestaof_route
from routes.gestaop import gestaop_route
from routes.login import login_route


def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home_route,url_prefix='/')
    app.register_blueprint(product_route,url_prefix='/products')
    app.register_blueprint(inventory_route,url_prefix='/inventories')
    app.register_blueprint(buy_route,url_prefix='/buys')
    app.register_blueprint(provider_route,url_prefix='/providers')
    app.register_blueprint(evaluation_route,url_prefix='/evaluations')
    app.register_blueprint(avaliacao_route,url_prefix='/avaliacao')
    app.register_blueprint(gestaop_route,url_prefix='/produtos')
    app.register_blueprint(gestaof_route,url_prefix='/fornecedores')
    app.register_blueprint(login_route,url_prefix='/login')



def configure_db():
    db.connect()
    db.create_tables([Product])
    db.create_tables([ProductProvider])
    db.create_tables([Inventory])
    db.create_tables([Buy])
    db.create_tables([Provider])
    db.create_tables([Evaluation])