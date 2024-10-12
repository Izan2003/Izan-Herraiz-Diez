## APP (relecloud)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations, name='destinations'),
    path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    path('cruise/<int:cruise_id>/', views.cruise_detail, name='cruise_detail'),
]