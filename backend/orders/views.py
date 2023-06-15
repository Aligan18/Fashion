from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from orders.models import Orders, OrderInfo
from orders.serializers import OrdersSerializers, OrderInfoSerializers, CreateOrderInfoSerializers, \
    CreateOrdersSerializers, AboutOrdersSerializers

# ORDER VIEWS
# Admin , Client
from testBackend.permissions import IsOwner


class OrdersAPICreate(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = CreateOrdersSerializers
    permission_classes = [IsAuthenticated]


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


# Admin , Client который сделал заказ
class OrdersAPIListAll(generics.ListAPIView):  # Все заказы Client автор
    queryset = Orders.objects.all()
    serializer_class = AboutOrdersSerializers
    permission_classes = [IsAdminUser, IsOwner]


# Admin
class OrdersAPIListAll(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = CreateOrdersSerializers
    permission_classes = [IsAdminUser]


#
# class OrdersAPIByUserId(generics.ListAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers


# ORDER INFO VIEWS
# Admin , Client
class OrderInfoAPICreate(generics.CreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = CreateOrderInfoSerializers
    permission_classes = [IsAuthenticated]


# Admin , Client если он автор заказа
class OrderInfoAPIRetrieve(generics.RetrieveAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializers
    permission_classes = [IsAdminUser, IsOwner]


# Admin
class OrderInfoAPIRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = CreateOrderInfoSerializers
    permission_classes = [IsAdminUser]