from flask import render_template, Blueprint, request
from peewee import DoesNotExist

from database.models.product import Product
from database.models.provider import Provider

from database.models.buy import Buy

buy_route = Blueprint('buy', __name__)

@buy_route.route('/')
def buys_list():
    buys = Buy.select()
    return render_template('buy/buys_list.html',buys=buys)

@buy_route.route('/', methods=['POST'])
def insert_buy():
    data = request.json
    try:
        product = Product.get_by_id(data['product_id'])
        provider = Provider.get_by_id(data['provider_id'])
    except Product.DoesNotExist:
        return "Produto não encontrado", 404
    except Provider.DoesNotExist:
        return "Fornecedor não encontrado", 404

    new_buy = Buy.create(
        date = data['date'],
        product = product,
        provider = provider,
        quantity = data['quantity'],
        cost = data['cost'],
    )

    return render_template('buy/buy_item.html', buy=new_buy, product=product, provider=provider)
@buy_route.route('/new')
def buy_form():
    providers = Provider.select()
    products = Product.select()
    return render_template('buy/buy_form.html',providers=providers, products=products)

@buy_route.route('/<int:buy_id>/edit')
def buy_edit_form(buy_id):
    buy = Buy.get_by_id(buy_id)
    providers = Provider.select()
    products = Product.select()
    return render_template('buy/buy_form.html',buy=buy,providers=providers, products=products)


@buy_route.route('/<int:buy_id>/update', methods=['PUT'])
def update_buy(buy_id):
    data = request.json

    buy_edited = Buy.get_by_id(buy_id)

    buy_edited.date = data['date']
    buy_edited.quantity = data['quantity']
    buy_edited.cost = data['cost']
    

    buy_edited.save()

    return render_template('buy/buy_item.html', buy = buy_edited)

@buy_route.route('/<int:buy_id>/delete', methods=['DELETE'])
def delete_buy(buy_id):
    buy = Buy.get_by_id(buy_id)
    buy.delete_instance()

    return render_template('buy/buy_form.html', deleted_buy = buy)