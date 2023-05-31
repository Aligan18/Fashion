from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from orders.models import Orders, OrderInfo
from orders.serializers import OrdersSerializers, OrderInfoSerializers


# ORDER VIEWS
class OrdersAPICreate(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers


class OrdersAPIRetrieve(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers


class OrdersAPIListAll(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializers

#
# class OrdersAPIByUserId(generics.ListAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializers


# ORDER INFO VIEWS

class OrderInfoAPIRetrieve(generics.RetrieveAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializers


class OrderInfoAPICreate(generics.CreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderInfoSerializers
