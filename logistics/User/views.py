from django.shortcuts import render
from .models import user , PickupRequest
from .serializers import UserSerializer , PickupSerializer
from rest_framework import generics 

class UserListCreate(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    
    
    
class UserRetrieve(generics.RetrieveAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    
class UserUpdate(generics.UpdateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    
class Userdelete(generics.DestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    
# pickup request
class PickupListCreate(generics.ListCreateAPIView):
    queryset = PickupRequest.objects.all()
    serializer_class = PickupSerializer
    def perform_create(self, serializer):
        serializer.save()
    
class pickupEdit(generics.RetrieveUpdateAPIView):
    queryset = PickupRequest.objects.all()
    serializer_class = PickupSerializer
class pickupDelete(generics.RetrieveDestroyAPIView):
    queryset = PickupRequest.objects.all()
    serializer_class = PickupSerializer
        
