## APP (relecloud)

from django.urls import path
from .views import (
    index, about, destinations, destination_detail, cruise_detail,
    DestinationCreateView, DestinationUpdateView, DestinationDeleteView
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('destinations/', destinations, name='destinations'),
    path('destination/<int:destination_id>/', destination_detail, name='destination_detail'),
    path('destination/add/', DestinationCreateView.as_view(), name='destination_add'),
    path('destination/<int:pk>/edit/', DestinationUpdateView.as_view(), name='destination_edit'),
    path('destination/<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination_delete'),
    path('cruise/<int:cruise_id>/', cruise_detail, name='cruise_detail'),
]