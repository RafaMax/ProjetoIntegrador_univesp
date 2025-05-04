from flask import Blueprint, render_template, request
from database.models.product import Product

product_route = Blueprint('product', __name__)

@product_route.route('/')
def products_list():
    products = Product.select()
    return render_template('product/products_list.html',products=products)

@product_route.route('/',methods=['POST'])
def insert_product():
    data = request.json

    new_product = Product.create(
        name = data['name'],
        category = data['category'],
        price = data['price'],
        quality = data['quality']

    )

    return  render_template('product/product_item.html', product = new_product)

@product_route.route('/new')
def product_form():
    return render_template('product/product_form.html')

@product_route.route('/<int:product_id>/edit')
def product_edit_form(product_id):
    product = Product.get_by_id(product_id)

    return render_template('product/product_form.html',product=product)


@product_route.route('/<int:product_id>/update',methods=['PUT'])
def update_product(product_id):
    data = request.json

    product_edited = Product.get_by_id(product_id)

    product_edited.name = data['name']
    product_edited.category = data['category']
    product_edited.price = data['price']
    product_edited.quality = data['quality']

    product_edited.save()

    return render_template('product/product_item.html', product = product_edited)

@product_route.route('/<int:product_id>/delete',methods=['DELETE'])
def delete_product(product_id):
    product = Product.get_by_id(product_id)
    product.delete_instance()

    return render_template('product/product_form.html', deleted_product = product)