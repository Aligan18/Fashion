from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from orders.models import Orders, OrderInfo
from orders.serializers import OrdersSerializers, OrderInfoSerializers


# ORDER VIEWS
# Admin , Client
class OrdersAPICreate(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers


# Admin , Client который сделал заказ
class OrdersAPIRetrieve(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers


# Admin
class OrdersAPIListAll(generics.ListAPIView): # Все заказы
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers


# Admin , Client который сделал заказ
class OrdersAPIListAll(generics.ListAPIView): # Все заказы Client автор
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers


# Admin
class OrdersAPIListAll(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers
#
# class OrdersAPIByUserId(generics.ListAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers


# ORDER INFO VIEWS
# Admin , Client
class OrderInfoAPICreate(generics.CreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializers


# Admin , Client если он автор заказа
class OrderInfoAPIRetrieve(generics.RetrieveAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializers


# Admin
class OrderInfoAPIRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializers



