from rest_framework import serializers

from clients.models import Clients
from products.models import Products, ProductInfo


class CreateProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CreateProductInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = '__all__'


class CreateBasketsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = 'basket'


class AboutProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class AboutBasketsSerializers(serializers.ModelSerializer):
    basket = AboutProductsSerializers(many=True)

    class Meta:
        model = Clients
        fields = 'basket'


class AboutProductInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = '__all__'
