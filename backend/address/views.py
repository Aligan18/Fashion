from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from address.models import Addresses
from address.serializers import AddressesSerializer, AboutAddressesSerializer, CreateAddressesSerializer

# Admin  Client
from testBackend.permissions import IsOwner


class AddressAPICreate(generics.CreateAPIView):
    queryset = Addresses.objects.all()
    serializer_class = CreateAddressesSerializer

    # permission_classes = IsAuthenticated

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()

    permission_classes = [IsAdminUser]


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
class AddressAPIUpdate(generics.UpdateAPIView):
    queryset = Addresses.objects.all()
    serializer_class = CreateAddressesSerializer
    permission_classes = [IsAdminUser | IsOwner]


# Admin ,   Client создатель
class AddressAPIDelete(generics.DestroyAPIView):
    queryset = Addresses.objects.all()
    serializer_class = CreateAddressesSerializer
    permission_classes = [IsAdminUser | IsOwner]
