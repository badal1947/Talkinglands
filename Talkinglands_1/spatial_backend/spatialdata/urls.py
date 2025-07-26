from django.urls import path
from .views import (
    PointListCreateView, PointRetrieveUpdateView,
    PolygonListCreateView, PolygonRetrieveUpdateView,
)

urlpatterns = [
    path('points/', PointListCreateView.as_view(), name='point-list-create'),
    path('points/<int:pk>/', PointRetrieveUpdateView.as_view(), name='point-detail-update'),
    path('polygons/', PolygonListCreateView.as_view(), name='polygon-list-create'),
    path('polygons/<int:pk>/', PolygonRetrieveUpdateView.as_view(), name='polygon-detail-update'),
]
