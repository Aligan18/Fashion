from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.
from baskets.models import Baskets
from baskets.serializers import BasketsSerializers


class BasketsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Baskets.objects.all()
    serializer_class = BasketsSerializers


class BasketsAPICreate(generics.CreateAPIView):
    queryset = Baskets.objects.all()
    serializer_class = BasketsSerializers
