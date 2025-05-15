from flask import Blueprint, render_template
from database.sqlconnector import compras_positivas

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    
    return render_template('index.html', compras_positivas = compras_positivas)