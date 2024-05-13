from rest_framework import serializers
from .models import user , PickupRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
        
class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickupRequest
        fields = '__all__'