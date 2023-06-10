from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from address.models import Addresses
from address.permissions import IsOwnerOrAdmin
from address.serializers import AddressesSerializer


class AddressAPICreate(generics.CreateAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer
    # permission_classes = IsAuthenticated


class AddressAPIRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer
    # permission_classes = IsOwnerOrAdmin
