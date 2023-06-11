from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.
from products.models import Baskets, Products, ProductInfo
from products.serializers import BasketsSerializers, ProductsSerializers, ProductInfoSerializers


# Admin , Client создатель
class BasketsAPIRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Baskets.objects.all()
    serializer_class = BasketsSerializers


# Products API
# Admin
class ProductsAPICreate(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


# All
class VisibleProductsAPIList(generics.ListAPIView):  # Только видемые
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


# Admin
class ProductsAPIList(generics.ListAPIView):  # Все товары
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


# All
class ProductsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


# All
class VisibleProductsAPIListByCategory(generics.ListAPIView):  # Фильтрация по категории
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


# Admin
class ProductsAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


# Product Info API


# All
class ProductInfoAPIRetrieve(generics.RetrieveAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializers


# Admin
class ProductInfoAPIUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializers
