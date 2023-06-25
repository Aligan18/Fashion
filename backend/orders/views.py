from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from orders.models import Orders, OrderInfo
from orders.serializers import OrdersSerializers, OrderInfoSerializers, CreateOrderInfoSerializers, \
    CreateOrdersSerializers, AboutOrdersSerializers
from orders.service import OrdersFilter
from testBackend.permissions import IsOwner, IsClient, IsOwnerForList


# ORDER VIEWS
# Admin , Client
class OrdersAPICreate(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = CreateOrdersSerializers
    permission_classes = [IsAuthenticated | IsClient]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrdersFilter


# ORDER INFO VIEWS
# Admin , Client
class OrderInfoAPICreate(generics.CreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = CreateOrderInfoSerializers
    permission_classes = [IsAuthenticated | IsClient]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


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
