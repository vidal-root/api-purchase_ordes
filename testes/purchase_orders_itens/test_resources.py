import json
def test_get_itens_by_purchase_order_id(test_client):
    response = test_client.get('/purchase_orders/1/itens')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['id'] == 1
    assert response.json[0]['description'] == 'Sabao'
    assert response.json[0]['price'] == 22.00


def test_get_itens_by_purchase_order_id_not_found(test_client):
    id = 999

    response = test_client.get('/purchase_orders/{}/itens'.format(id))

    assert response.status_code == 200
    assert response.json['message'] == 'Pedido de id {} nao encontrado'.format(id)


def test_post_purchase_order_item(test_client):
    obj = {
        'id': 1,
        'description': 'Sabao',
        'price': 22.00
    }

    response = test_client.post('/purchase_orders/1/itens', data=json.dumps(obj), content_type='application/json')

    assert response.status_code == 200
    assert response.json['id'] == 1
    assert response.json['itens'][1]['id'] == obj['id']

def test_post_invalid_id(test_client):
    obj = {
        'description': 'Item teste',
        'price': 10.0
    }

    response = test_client.post('/purchase_orders/1/itens', data=json.dumps(obj), content_type='application/json')

    assert response.status_code == 400
    assert response.json['message']['id'] == 'Informe um id valido'

def test_post_invalid_description(test_client):
    obj = {
        'id': 2,
        'price': 10.0
    }

    response = test_client.post('/purchase_orders/1/itens', data=json.dumps(obj), content_type='application/json')

    assert response.status_code == 400
    assert response.json['message']['description'] == 'Informe uma descricao'


