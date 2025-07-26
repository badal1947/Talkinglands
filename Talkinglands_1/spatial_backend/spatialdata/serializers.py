from rest_framework import serializers
from .models import PointData, PolygonData

class PointDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointData
        fields = '__all__'

class PolygonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolygonData
        fields = '__all__'
