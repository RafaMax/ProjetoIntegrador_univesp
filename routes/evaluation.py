from flask import render_template, Blueprint, request
from collections import defaultdict
from database.models.evaluation import Evaluation
from database.models.buy import Buy
from database.models.product import Product

evaluation_route = Blueprint('evaluation', __name__)

@evaluation_route.route('/')
def evaluations_list():
    evaluations = Evaluation.select()
    return render_template('evaluation/evaluations_list.html',evaluations=evaluations)

@evaluation_route.route('/', methods=['POST'])
def insert_evaluation():
    data = request.json

    new_evaluation = Evaluation.create(
        buy_id = data['buy_id'],
        product_id = data['product_id'],
        quantidade_avaliada = data['quantidade_avaliada'],
        qualidade_avaliada = data['qualidade_avaliada']

    )

    return  render_template('evaluation/evaluation_item.html', evaluation = new_evaluation)

@evaluation_route.route('/new')
def evaluation_form():
    buys = Buy.select()
    products_by_date = defaultdict(list)
    # Agrupando os produtos por data de compra
    # Para cada compra, adiciona o produto à lista correspondente à data
    for buy in buys:
        # Use str(buy.date) para garantir que a chave seja igual ao value do <option>
        date_str = buy.date.strftime('%Y-%m-%d')
        products_by_date[date_str].append({'id': buy.product.id, 'name': buy.product.name})
    return render_template(
        'evaluation/evaluation_form.html',
        buys=buys,
        products_by_date=products_by_date
    )
@evaluation_route.route('/<int:evaluation_id>/edit')
def evaluation_edit_form(evaluation_id):
    evaluation = Evaluation.get_by_id(evaluation_id)
    buys = Buy.select()
    products_by_date = defaultdict(list)
    for buy in buys:
        date_str = buy.date.strftime('%Y-%m-%d')
        products_by_date[date_str].append({'id': buy.product.id, 'name': buy.product.name})
    return render_template(
        'evaluation/evaluation_form.html',
        evaluation=evaluation,
        buys=buys,
        products_by_date=products_by_date
    )


@evaluation_route.route('/<int:evaluation_id>/update', methods=['PUT'])
def update_evaluation(evaluation_id):
    data = request.json

    evaluation_edited = Evaluation.get_by_id(evaluation_id)

    evaluation_edited.buy_id = data['buy_id']
    evaluation_edited.product_id = data['product_id']
    evaluation_edited.quantidade_avaliada = data['quantidade_avaliada']
    evaluation_edited.qualidade_avaliada = data['qualidade_avaliada']

    evaluation_edited.save()

    return render_template('evaluation/evaluation_item.html', evaluation = evaluation_edited)

@evaluation_route.route('/<int:evaluation_id>/delete', methods=['DELETE'])
def delete_evaluation(evaluation_id):
    evaluation = Evaluation.get_by_id(evaluation_id)
    evaluation.delete_instance()

    return render_template('evaluation/evaluation_form.html', deleted_evaluation = evaluation)