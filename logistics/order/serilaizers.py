from rest_framework import serializers
from .models import order


class orderSerializer(serializers.ModelSerializer):
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
            'cash_on_delivery', 
            'shipping_price',
            'net_income',
            'order_status',
        ]
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['shipper'] = {
            "id":instance.shipper.user.id,
            "username":instance.shipper.user.username,
            "email":instance.shipper.user.email,
            "phone":instance.shipper.phone,
            }
        return rep
