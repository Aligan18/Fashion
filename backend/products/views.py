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

class VisibleProductsAPIList(generics.ListAPIView):  # Только видемые
    queryset = Products.objects.all()
    serializer_class = AboutProductsSerializers
    permission_classes = [AllowAny]


# Admin
class ProductsAPIList(generics.ListAPIView):  # Все товары
    queryset = Products.objects.all()
    serializer_class = AboutProductsSerializers
    permission_classes = [IsAdminUser]


# All
class ProductsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [AllowAny]


# All
class VisibleProductsAPIListByCategory(generics.ListAPIView):  # Фильтрация по категории
    queryset = Products.objects.all()
    serializer_class = AboutProductsSerializers
    permission_classes = [AllowAny]


# Admin
class ProductsAPIUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = CreateProductsSerializers
    permission_classes = [IsAdminUser]


# Product Info API #################################################################################

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
