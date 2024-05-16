from rest_framework import serializers
from .models import AppUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
        
# class PickupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PickupRequest
#         fields = '__all__'