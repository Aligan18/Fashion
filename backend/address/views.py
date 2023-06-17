from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from address.models import Addresses
from address.serializers import AddressesSerializer, AboutAddressesSerializer, CreateAddressesSerializer
from testBackend.permissions import IsOwner, IsClient


# Admin  Client
class AddressAPICreate(generics.CreateAPIView):
    queryset = Addresses.objects.all()
    serializer_class = CreateAddressesSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

    permission_classes = [IsAdminUser | IsClient]


# Admin
class AddressAPIList(generics.ListAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AboutAddressesSerializer
    permission_classes = [IsAdminUser]


# Admin ,   Client создатель
class AddressAPIRetrieve(generics.RetrieveAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer
    permission_classes = [IsAdminUser | IsOwner]


# Admin ,   Client создатель
class AddressAPIRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Addresses.objects.all()
    serializer_class = CreateAddressesSerializer
    permission_classes = [IsAdminUser | IsOwner]

