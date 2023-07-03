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


class PurchaseOrdersItens(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help='Informe um id valido')
    parser.add_argument('description', type=str, required=True, help='Informe uma descricao')
    parser.add_argument('price', type=float, required=True, help='Informe um preco')

    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po['itens'])

        return jsonify({'message': 'Pedido de id {} nao encontrado'.format(id)})

    def post(self, id):
        data = PurchaseOrdersItens().parser.parse_args()
        for po in purchase_orders:
            if po['id'] == id:
                po['itens'].append(
                    {
                        'id': data['id'],
                        'description': data['description'],
                        'price': data['price']
                    }
                )

                return jsonify(po)

            return jsonify({'message': 'Este pedido nao existe'})
