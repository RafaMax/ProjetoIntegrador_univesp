from flask import Blueprint, render_template
from database.models.product import Product
from database.models.evaluation import Evaluation
from flask import jsonify
home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    total = Product.select().count()
    quantidade_muita = Evaluation.select().where(Evaluation.quantidade_avaliada == "Muita").count()
    quantidade_pouca = Evaluation.select().where(Evaluation.quantidade_avaliada == "Pouca").count()
    quantidade_ideal = Evaluation.select().where(Evaluation.quantidade_avaliada == "Ideal").count()
    produtos =Product.select()
    return render_template('index.html',Total=total,Produtos=produtos, quantidade_muita=quantidade_muita, quantidade_pouca=quantidade_pouca, quantidade_ideal=quantidade_ideal)

@home_route.route('/quantidade_muita')
def quantidade_muita():
    avaliacoes = (Evaluation.select().where(Evaluation.quantidade_avaliada == "Muita"))
    result = []
    for av in avaliacoes:
        result.append({
            "produto": av.product.name,
            
            "data_compra": av.buy.date.strftime('%d/%m/%Y'),  # Data da compra
            
        })
    return jsonify(result)

@home_route.route('/quantidade_pouca')
def quantidade_pouca():
    avaliacoes = (Evaluation.select().where(Evaluation.quantidade_avaliada == "Pouca"))
    result = []
    for av in avaliacoes:
        result.append({
            "produto": av.product.name,
            "data_compra": av.buy.date.strftime('%d/%m/%Y'),  # Data da compra
        })
    return jsonify(result)

@home_route.route('/quantidade_ideal')
def quantidade_ideal():
    avaliacoes = (Evaluation.select().where(Evaluation.quantidade_avaliada == "Ideal"))
    result = []
    for av in avaliacoes:
        result.append({
            "produto": av.product.name,
            "data_compra": av.buy.date.strftime('%d/%m/%Y'),  # Data da compra
        })
    return jsonify(result)
    