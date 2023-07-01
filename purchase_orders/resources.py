from flask import jsonify
from flask_restful import Resource

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido 1',
        'itens': [
            {
                'id': 1,
                'description': 'Sabao',
                'price': 22.00
            }
        ]
    }
]


class PurchaseOrders(Resource):
    def get(self):
        return jsonify(purchase_orders)
