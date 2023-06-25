from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
# Create your views here.
from rest_framework.permissions import IsAdminUser, AllowAny

from clients.models import Clients
from products.models import Products, ProductInfo
from products.serializers import ProductsSerializers, ProductInfoSerializers, \
    CreateProductsSerializers, CreateBasketsSerializers, AboutProductsSerializers, CreateProductInfoSerializers, \
    AboutBasketsSerializers

#################################################################################
# Admin , Client создатель
from products.service import ProductsFilter
from testBackend.permissions import IsOwner


class BasketsAPIRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Clients.objects.all()
    serializer_class = CreateBasketsSerializers
    permission_classes = [IsAdminUser, IsOwner]


class BasketsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Clients.objects.all()
    serializer_class = AboutBasketsSerializers
    permission_classes = [IsAdminUser, IsOwner]


# Products API #################################################################################

# Admin
class ProductsAPICreate(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = CreateProductsSerializers
    permission_classes = [IsAdminUser]


# All


class VisibleProductsAPIList(generics.ListAPIView):  # Только видимые добавить фильрацию по категории
    queryset = Products.objects.filter(visible=True)
    serializer_class = AboutProductsSerializers
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductsFilter


# Admin
class ProductsAPIList(generics.ListAPIView):  # Все товары добавить фильрацию по категории
    queryset = Products.objects.all()
    serializer_class = AboutProductsSerializers
    permission_classes = [IsAdminUser]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductsFilter


# All
class ProductsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [AllowAny]


# Admin
class ProductsAPIUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = CreateProductsSerializers
    permission_classes = [IsAdminUser]


# Product Info API #################################################################################
# Admin
class ProductInfoAPICreate(generics.CreateAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializers
    permission_classes = [IsAdminUser]


# All
class ProductInfoAPIRetrieve(generics.RetrieveAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializers
    permission_classes = [AllowAny]


# Admin
class ProductInfoAPIUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = CreateProductInfoSerializers
    permission_classes = [IsAdminUser]
#################################################################################
