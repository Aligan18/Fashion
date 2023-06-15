from rest_framework import serializers
from orders.models import Orders, OrderInfo


class CreateOrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class CreateOrderInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'


class AboutOrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class AboutOrderInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'


class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'

