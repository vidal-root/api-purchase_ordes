import pytz
from flask import jsonify
from flask_restful import Resource, reqparse
from model import PurchaseOrderModel


class PurchaseOrders(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('description', type=str, required=True, help='Informe uma descrição')

    def get(self):
        purchase_orders = PurchaseOrderModel.fill_all()
        return [p.as_dict() for p in purchase_orders]

    def post(self):
        data = PurchaseOrders.parser.parse_args()

        purchase_orders = PurchaseOrderModel(**data)

        return 


class PurchaseOrderById(Resource):
    def get(self, id):
        for po in purchase_orders:
            if po['id'] == id:
                return jsonify(po)

        return jsonify({'message': 'Pedido de id {} nao encontrado'.format(id)})
