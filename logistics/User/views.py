from django.shortcuts import render
from .models import user
from .serializers import UserSerializer
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