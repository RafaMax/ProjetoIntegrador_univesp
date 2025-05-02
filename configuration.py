from database.database import db
from database.models.buy import Buy
from database.models.climate import Climate
from database.models.inventory import Inventory
from database.models.product import Product
from database.models.provider import Provider
from routes.buy import buy_route
from routes.climate import climate_route
from routes.home import home_route
from routes.inventory import inventory_route
from routes.product import product_route
from routes.provider import provider_route


def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(product_route,url_prefix='/products')
    app.register_blueprint(inventory_route,url_prefix='/inventories')
    app.register_blueprint(buy_route,url_prefix='/buys')
    app.register_blueprint(climate_route,url_prefix='/climates')
    app.register_blueprint(provider_route,url_prefix='/providers')


def configure_db():
    db.connect()
    db.create_tables([Product])
    db.create_tables([Inventory])
    db.create_tables([Buy])
    db.create_tables([Climate])
    db.create_tables([Provider])