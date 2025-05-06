from flask import Blueprint, render_template

gestaof_route = Blueprint('fornecedores', __name__)

@gestaof_route.route('/')
def gestaof():
    return render_template('sidebar/gestaof.html')