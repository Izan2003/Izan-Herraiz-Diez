from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django import forms
from .models import Destination, Cruise

# Define the form directly in views.py
class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description']

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

def destination_detail(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    cruises = Cruise.objects.filter(destination=destination)
    return render(request, 'destination_detail.html', {'destination': destination, 'cruises': cruises})

def cruise_detail(request, cruise_id):
    cruise = get_object_or_404(Cruise, id=cruise_id)
    return render(request, 'cruise_detail.html', {'cruise': cruise})

class DestinationCreateView(CreateView):
    model = Destination
    form_class = DestinationForm
    template_name = 'destination_form.html'
    success_url = reverse_lazy('destinations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Destination'
        context['button_text'] = 'Add Destination'
        return context

class DestinationUpdateView(UpdateView):
    model = Destination
    form_class = DestinationForm
    template_name = 'destination_form.html'
    success_url = reverse_lazy('destinations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Destination'
        context['button_text'] = 'Update Destination'
        return context

class DestinationDeleteView(DeleteView):
    model = Destination
    template_name = 'destination_confirm_delete.html'
    success_url = reverse_lazy('destinations')