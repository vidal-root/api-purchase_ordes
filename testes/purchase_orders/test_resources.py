def test_get_purchase_orders(test_client):
    response = test_client.get('purchase_orders')

    assert response.status_code == 200
    assert response.json[0]['id'] == 1
