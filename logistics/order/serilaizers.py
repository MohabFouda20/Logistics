from rest_framework import serializers
from .models import order


class orderSerializer(serializers.ModelSerializer):
    NetIncome  = serializers.SerializerMethodField()
    class Meta:
        model = order
        fields = [
            'shipper',
            'id',
            'name',
            'phone',
            'government',
            'address',
            'shipment_content',
            'cod', 
            'shipping_price',
            'NetIncome',
        ]

    def get_NetIncome(self, order):
        net_income = order.cod - order.shipping_price
        return net_income