from flask import render_template, Blueprint, request

from database.models.climate import Climate

climate_route = Blueprint('climate', __name__)

@climate_route.route('/')
def climates_list():
    climate = Climate.select()
    return render_template('climate/climates_list.html',climate=climate)

@climate_route.route('/', methods=['POST'])
def insert_climate():
    data = request.json

    new_climate = Climate.create(
        date = data['date'],
        temperature = data['temperature'],
        product_impact = data['product_impact']

    )

    return  render_template('climate/climate_item.html', climate = new_climate)

@climate_route.route('/new')
def climate_form():
    return render_template('climate/climate_form.html')

@climate_route.route('/<int:climate_id>/edit')
def climate_edit_form(climate_id):
    climate = Climate.get_by_id(climate_id)

    return render_template('climate/climate_form.html',climate=climate)


@climate_route.route('/<int:climate_id>/update', methods=['PUT'])
def update_climate(climate_id):
    data = request.json

    climate_edited = Climate.get_by_id(climate_id)

    climate_edited.date = data['date']
    climate_edited.temperature = data['temperature']
    climate_edited.product_impact = data['product_impact']

    climate_edited.save()

    return render_template('climate/climate_item.html', climate = climate_edited)

@climate_route.route('/<int:climate_id>/delete', methods=['DELETE'])
def delete_climate(climate_id):
    climate = Climate.get_by_id(climate_id)
    climate.delete_instance()

    return render_template('climate/climate_form.html', deleted_climate = climate)