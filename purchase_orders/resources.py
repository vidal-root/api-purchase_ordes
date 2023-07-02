from flask import jsonify
from flask_restful import Resource, reqparse

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
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help='Informe um id valido')
    parser.add_argument('description', type=str, required=True, help='Informe uma descrição')

    def get(self):
        return jsonify(purchase_orders)

    def post(self):
        data = PurchaseOrders.parser.parse_args()

        purchase_order = {
            'id': data['id'],
            'description': data['description'],
            'itens': []
        }

        purchase_orders.append(purchase_order)

        return jsonify(purchase_order)


class PurchaseOrderById(Resource):
    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po)

        return jsonify({'message': 'Pedido de id {} nao encontrado'.format(id)})
