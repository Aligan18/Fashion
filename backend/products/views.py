from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.
from products.models import Baskets
from products.serializers import BasketsSerializers


class BasketsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Baskets.objects.all()
    serializer_class = BasketsSerializers


class BasketsAPICreate(generics.CreateAPIView):
    queryset = Baskets.objects.all()
    serializer_class = BasketsSerializers
