from flask import Blueprint, render_template

avaliacao_route = Blueprint('avaliacao', __name__)

@avaliacao_route.route('/')
def avaliacao():
    return render_template('sidebar/avaliacao.html')