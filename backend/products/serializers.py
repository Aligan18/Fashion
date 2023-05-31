from rest_framework import serializers

from products.models import Baskets, Products, ProductInfo


class BasketsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Baskets
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = '__all__'
