from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class DevicedIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('device_id')