from database.database import db
from database.models.product import Product
from routes.home import home_route
from routes.product import product_route


def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(product_route,url_prefix='/products')


def configure_db():
    db.connect()
    db.create_tables([Product])