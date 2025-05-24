from flask import render_template, Blueprint, request
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
    # Verifica se existe uma compra para o produto selecionado
    has_buy = Buy.select().where(Buy.product == data['product_id']).exists()
    if not has_buy:
        return "Produto não possui compra cadastrada!", 400

    new_evaluation = Evaluation.create(
        buy_id = data['buy_id'],
        product_id = data['product_id'],
        quantidade_avaliada = data['quantidade_avaliada'],
        qualidade_avaliada = data['qualidade_avaliada']
    )
    return render_template('evaluation/evaluation_item.html', evaluation = new_evaluation)

@evaluation_route.route('/new')
def evaluation_form():
    buys = Buy.select()
    products = Product.select()
    return render_template(
        'evaluation/evaluation_form.html',
        buys=buys,
        products=products
    )
@evaluation_route.route('/<int:evaluation_id>/edit')
def evaluation_edit_form(evaluation_id):
    evaluation = Evaluation.get_by_id(evaluation_id)
    buys = Buy.select()
    products = Product.select()
    return render_template(
        'evaluation/evaluation_form.html',
        evaluation=evaluation,
        buys=buys,
        products=products
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