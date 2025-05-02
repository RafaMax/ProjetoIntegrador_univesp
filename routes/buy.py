from flask import render_template, Blueprint, request

from database.models.buy import Buy

buy_route = Blueprint('buy', __name__)

@buy_route.route('/')
def buys_list():
    buy = Buy.select()
    return render_template('buy/buys_list.html',buy=buy)

@buy_route.route('/', methods=['POST'])
def insert_buy():
    data = request.json

    new_buy = Buy.create(
        date = data['date'],
        quantity = data['quantity'],
        product_id = data['product_id'],
        provider_id = data['provider_id'],
        cost = data['cost'],
        user_id = data['user_id']

    )

    return  render_template('buy/buy_item.html', buy = new_buy)

@buy_route.route('/new')
def buy_form():
    return render_template('buy/buy_form.html')

@buy_route.route('/<int:buy_id>/edit')
def buy_edit_form(buy_id):
    buy = Buy.get_by_id(buy_id)

    return render_template('buy/buy_form.html',buy=buy)


@buy_route.route('/<int:buy_id>/update', methods=['PUT'])
def update_buy(buy_id):
    data = request.json

    buy_edited = Buy.get_by_id(buy_id)

    buy_edited.date = data['date']
    buy_edited.quantity = data['quantity']
    buy_edited.product_id = data['product_id']
    buy_edited.provider_id = data['provider_id']
    buy_edited.cost = data['cost']
    buy_edited.user_id = data['user_id']

    buy_edited.save()

    return render_template('buy/buy_item.html', buy = buy_edited)

@buy_route.route('/<int:buy_id>/delete', methods=['DELETE'])
def delete_buy(buy_id):
    buy = Buy.get_by_id(buy_id)
    buy.delete_instance()

    return render_template('buy/buy_form.html', deleted_buy = buy)