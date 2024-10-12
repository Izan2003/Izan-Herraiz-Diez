from django.shortcuts import render, HttpResponse, get_object_or_404
from . import models
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

def cruise_detail(request, cruise_id):
    cruise = get_object_or_404(models.Cruise, id=cruise_id)
    return render(request, 'cruise_detail.html', {'cruise': cruise})


def destination_detail(request, destination_id):
    destination = get_object_or_404(models.Destination, id=destination_id)
    cruises = models.Cruise.objects.filter(destination=destination)
    return render(request, 'destination_detail.html', {'destination': destination, 'cruises': cruises})

def cruise_detail(request, cruise_id):
    cruise = get_object_or_404(models.Cruise, id=cruise_id)
    return render(request, 'cruise_detail.html', {'cruise': cruise})