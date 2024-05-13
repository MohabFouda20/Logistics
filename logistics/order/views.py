from django.shortcuts import render
from rest_framework import generics
from .models import order
from .serilaizers import orderSerializer
# Create your views here.
class orderListCreate(generics.ListCreateAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        

class OrderRetrieve(generics.RetrieveAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer
    
    
class OrderUpdate(generics.RetrieveUpdateAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer


class OrderDelete(generics.RetrieveDestroyAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer  