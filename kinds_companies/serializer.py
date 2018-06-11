from rest_framework import serializers
from .models import Kind_Company

class KindCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind_Company
        fields = '__all__'
