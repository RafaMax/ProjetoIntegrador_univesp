from flask import render_template, Blueprint, request

from database.models.evaluation import Evaluation

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
        note=data['note'],
        ranking = data['ranking']

    )

    return  render_template('evaluation/evaluation_item.html', evaluation = new_evaluation)

@evaluation_route.route('/new')
def evaluation_form():
    return render_template('evaluation/evaluation_form.html')

@evaluation_route.route('/<int:evaluation_id>/edit')
def evaluation_edit_form(evaluation_id):
    evaluation = Evaluation.get_by_id(evaluation_id)

    return render_template('evaluation/evaluation_form.html',evaluation=evaluation)


@evaluation_route.route('/<int:evaluation_id>/update', methods=['PUT'])
def update_evaluation(evaluation_id):
    data = request.json

    evaluation_edited = Evaluation.get_by_id(evaluation_id)

    evaluation_edited.buy_id = data['buy_id']
    evaluation_edited.note = data['note']
    evaluation_edited.ranking = data['ranking']

    evaluation_edited.save()

    return render_template('evaluation/evaluation_item.html', evaluation = evaluation_edited)

@evaluation_route.route('/<int:evaluation_id>/delete', methods=['DELETE'])
def delete_evaluation(evaluation_id):
    evaluation = Evaluation.get_by_id(evaluation_id)
    evaluation.delete_instance()

    return render_template('evaluation/evaluation_form.html', deleted_evaluation = evaluation)