from flask import Blueprint, render_template
from database.models.product import Product

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    total = Product.select().count()
    produtos =Product.select()
    return render_template('index.html',Total=total,Produtos=produtos)