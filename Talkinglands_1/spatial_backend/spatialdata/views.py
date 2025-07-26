# from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import PointData, PolygonData
from .serializers import PointDataSerializer, PolygonDataSerializer

class PointListCreateView(generics.ListCreateAPIView):
    queryset = PointData.objects.all()
    serializer_class = PointDataSerializer

class PointRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PointData.objects.all()
    serializer_class = PointDataSerializer

class PolygonListCreateView(generics.ListCreateAPIView):
    queryset = PolygonData.objects.all()
    serializer_class = PolygonDataSerializer

class PolygonRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PolygonData.objects.all()
    serializer_class = PolygonDataSerializer
