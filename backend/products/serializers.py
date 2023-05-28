from rest_framework import serializers

from products.models import Baskets


class BasketsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Baskets
        fields = '__all__'
