from flask import Blueprint, render_template

gestaop_route = Blueprint('produtos', __name__)

@gestaop_route.route('/')
def gestaop():
    
    return render_template('sidebar/gestaop.html')