from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.
from .models import Users
from .models import Products
from .serializers import UsersSerializer
from .serializers import ProductsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
