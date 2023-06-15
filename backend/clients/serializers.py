from rest_framework import serializers

from .models import Clients


class CreateClientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class ClientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class AboutClientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
