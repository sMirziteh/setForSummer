from django.shortcuts import render, redirect, HttpResponse
import random
from .models import Users, Location


def setHome(request):
    new_list = []
    distinct = Users.objects.values('zipcode').distinct()

    for data in distinct:
        obj = {
            'zip': data['zipcode'],
            'count': Users.objects.filter( zipcode = data['zipcode']).count()
        }
        new_list.append(obj)
    data = {
        'data': Users.objects.values('zipcode').distinct(),
        'rand': random.randrange(1,10),
        'list': new_list
    }
    
    return render(request, 'setForSummer_app/index.html', data)

def food(request):
    places = Location.objects.filter(category = 'food')
    lastplace = Location.objects.filter(category = 'food').last()
    last= str(lastplace.id)
    return render(request, 'setForSummer_app/food.html', {'lastID':last,'places':places})

def activities(request):
    places = {
        'places': Location.objects.filter(category = 'activity')
    }
    return render(request, 'setForSummer_app/activities.html', places)

def learning(request):
    places = Location.objects.filter(category = 'education')
    lastplace = Location.objects.filter(category = 'education').last()
    last= str(lastplace.id)
    return render(request, 'setForSummer_app/learning.html', {'lastID':last,'places':places})

def faqs(request):
    return render(request, 'setForSummer_app/faqs.html')

def contact(request):
    return render(request, 'setForSummer_app/contact.html')

def activities_map(request,id):
    map = Location.objects.get(id=id)
    return render(request,'setForSummer_app/map2.html',{
        'map_id': map.id,
        'lat':map.lat,
        'lon':map.lon,
    })

def map_id(request,id):
    map = Location.objects.get(id=id)
    return render(request,'setForSummer_app/map.html',{
        'id': map.id,
        'lat':map.lat,
        'lon':map.lon,
    })

def signup(request):
    result = Users.objects.signupform(request.POST)
    if type(result) is dict:
        result = 'worked!'
        print(result)
    return HttpResponse()
    
    