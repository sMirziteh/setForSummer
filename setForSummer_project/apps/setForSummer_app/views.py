from django.shortcuts import render, redirect, HttpResponse
from .models import *


def setHome(request):
    # return HttpResponse('you made it home')
    return render(request, 'setForSummer_app/index.html')

def food(request):
    map = Location.objects.get(id=8)
    coords = {
        'lat': map.lat,
        'lng': map.lon
    }
    print(coords)

    return render(request, 'setForSummer_app/food.html', coords)

def activities(request):
    return render(request, 'setForSummer_app/activites.html')

def map(request):
    return HttpResponse()
