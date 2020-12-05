from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import PuestoTrabajo, Item
from django.http import HttpResponse 
from . import views
from .resources import PuestoTrabajoResource

class HomeView(ListView):
    model = PuestoTrabajo
    template_name = "item/home.html"
    context_object_name = 'equipo'
    #queryset = DepaPuesto.objects.all()

def export(request):
    puestotrabajo_resource = PuestoTrabajoResource()
    dataset = puestotrabajo_resource.export(request)
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="activohardware.csv"'
    return response


