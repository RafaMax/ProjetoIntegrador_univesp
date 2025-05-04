from flask import render_template, Blueprint, request

from database.models.inventory import Inventory

inventory_route = Blueprint('inventory', __name__)

@inventory_route.route('/')
def inventories_list():
    inventories = Inventory.select()
    return render_template('inventory/inventories_list.html',inventories=inventories)

@inventory_route.route('/', methods=['POST'])
def insert_inventory():
    data = request.json

    new_inventory = Inventory.create(
        product_id = data['product_id']
    )

    return  render_template('inventory/inventory_item.html', inventory = new_inventory)

@inventory_route.route('/new')
def inventory_form():
    return render_template('inventory/inventory_form.html')

@inventory_route.route('/<int:inventory_id>/edit')
def inventory_edit_form(inventory_id):
    inventory = Inventory.get_by_id(inventory_id)

    return render_template('inventory/inventory_form.html',inventory=inventory)


@inventory_route.route('/<int:inventory_id>/update', methods=['PUT'])
def update_inventory(inventory_id):
    data = request.json

    inventory_edited = Inventory.get_by_id(inventory_id)

    inventory_edited.product_id = data['product_id']

    inventory_edited.save()

    return render_template('inventory/inventory_item.html', inventory = inventory_edited)

@inventory_route.route('/<int:inventory_id>/delete', methods=['DELETE'])
def delete_inventory(inventory_id):
    inventory = Inventory.get_by_id(inventory_id)
    inventory.delete_instance()

    return render_template('inventory/inventory_form.html', deleted_inventory = inventory)