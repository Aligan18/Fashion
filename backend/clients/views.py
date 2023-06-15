
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from clients.models import Clients
from clients.serializers import AboutClientsSerializers, ClientsSerializers, CreateClientsSerializers


# Admin
from testBackend.permissions import IsOwner


class ClientsViewAll(generics.ListAPIView):  # Вообще все клиенты
    queryset = Clients.objects.all()
    serializer_class = AboutClientsSerializers
    permission_classes = [IsAdminUser]


# Authorized
class ClientsViewRetrieve(generics.RetrieveAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializers
    permission_classes = [IsAuthenticated]


# Client  свой профиль
class ClientsViewUpdate(generics.UpdateAPIView):
    queryset = Clients.objects.all()
    serializer_class = CreateClientsSerializers
    permission_classes = [IsOwner]


# Admin,  Client свой профиль
class ClientsViewDestroy(generics.DestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = CreateClientsSerializers
    permission_classes = [IsAdminUser | IsOwner]
