# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Carro, Fabricante

# Create your views here.

def carros(request):
    todos_carros = Carro.objects.all()
    return render(request, 'carros/carros.html', {'carros': todos_carros})

def detail(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    return render(request, 'carros/details.html', {'item': carro})

def fabricantes(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'carros/fabricantes.html', {'fabricantes': fabricantes})
