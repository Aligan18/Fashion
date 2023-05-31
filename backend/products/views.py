from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.
from products.models import Baskets, Products, ProductInfo
from products.serializers import BasketsSerializers, ProductsSerializers, ProductInfoSerializers


class BasketsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Baskets.objects.all()
    serializer_class = BasketsSerializers


class BasketsAPICreate(generics.CreateAPIView):
    queryset = Baskets.objects.all()
    serializer_class = BasketsSerializers


# Products API
# class ProductsAPIVisibleList(generics.ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializers

# class ProductsAPIVisibleByID(generics.ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializers

class ProductsAPIListAll(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


# class ProductsAPIVisibleListByCategory(generics.ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializers


class ProductsAPICreate(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


class ProductsAPIDelete(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers


# Product Info API
class ProductInfoAPIRetrieve(generics.RetrieveAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializers


class ProductInfoAPIUpdate(generics.UpdateAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializers


class ProductInfoAPICreate(generics.CreateAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializers
