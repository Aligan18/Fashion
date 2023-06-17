from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from orders.models import Orders, OrderInfo
from orders.serializers import OrdersSerializers, OrderInfoSerializers, CreateOrderInfoSerializers, \
    CreateOrdersSerializers, AboutOrdersSerializers
from testBackend.permissions import IsOwner, IsClient, IsOwnerForList


# ORDER VIEWS
# Admin , Client
class OrdersAPICreate(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = CreateOrdersSerializers
    permission_classes = [IsAuthenticated | IsClient]


# Admin , Client который сделал заказ
class OrdersAPIRetrieve(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers
    permission_classes = [IsAdminUser, IsOwner]


# Admin
class OrdersAPIListAll(generics.ListAPIView):  # Все заказы
    queryset = Orders.objects.all()
    serializer_class = AboutOrdersSerializers
    permission_classes = [IsAdminUser]


# Admin
class OrdersAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = CreateOrdersSerializers
    permission_classes = [IsAdminUser]


# Admin , is Owner
class OrdersAPIByUserId(generics.ListAPIView):  # все заказы одного клиента
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers
    permission_classes = [IsAdminUser | IsOwnerForList]


# ORDER INFO VIEWS
# Admin , Client
class OrderInfoAPICreate(generics.CreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = CreateOrderInfoSerializers
    permission_classes = [IsAuthenticated | IsClient]


# Admin , Client если он автор заказа
class OrderInfoAPIRetrieve(generics.RetrieveAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializers
    permission_classes = [IsAdminUser, IsOwner]


# Admin
class OrderInfoAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = CreateOrderInfoSerializers
    permission_classes = [IsAdminUser]
