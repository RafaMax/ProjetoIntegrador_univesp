from flask import render_template, Blueprint, request

from database.models.provider import Provider


provider_route = Blueprint('provider', __name__)

@provider_route.route('/')
def providers_list():
    providers = Provider.select()
    return render_template('provider/providers_list.html',providers=providers)

@provider_route.route('/', methods=['POST'])
def insert_provider():
    data = request.json

    new_provider = Provider.create(
        name = data['name'],
        

    )

    return  render_template('provider/provider_item.html', provider = new_provider)

@provider_route.route('/new')
def provider_form():
    return render_template('provider/provider_form.html')

@provider_route.route('/<int:provider_id>/edit')
def provider_edit_form(provider_id):
    provider = Provider.get_by_id(provider_id)

    return render_template('provider/provider_form.html',provider=provider)


@provider_route.route('/<int:provider_id>/update', methods=['PUT'])
def update_provider(provider_id):
    data = request.json

    provider_edited = Provider.get_by_id(provider_id)

    provider_edited.name = data['name']
    

    provider_edited.save()

    return render_template('provider/provider_item.html', provider = provider_edited)

@provider_route.route('/<int:provider_id>/delete', methods=['DELETE'])
def delete_provider(provider_id):
    provider = Provider.get_by_id(provider_id)
    provider.delete_instance()

    return render_template('provider/provider_form.html', deleted_provider = provider)