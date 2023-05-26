from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from address.models import Addresses
from address.serializers import AddressesSerializer


class AddressAPICreate(generics.CreateAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer


class AddressAPIList(generics.RetrieveAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer
