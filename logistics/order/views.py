from django.shortcuts import render
from rest_framework import generics
from .models import order
from .serilaizers import orderSerializer
# Create your views here.
class orderListCreate(generics.ListCreateAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer