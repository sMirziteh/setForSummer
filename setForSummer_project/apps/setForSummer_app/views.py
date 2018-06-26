from django.shortcuts import render, redirect, HttpResponse


def setHome(request):
    # return HttpResponse('you made it home')
    return render(request, 'setForSummer_app/index.html')

def food(request):
    return render(request, 'setForSummer_app/food.html')

def activities(request):
    return render(request, 'setForSummer_app/activites.html')

def map_html(request,id):
    map = Location.objects.get(id=id)
    return render(request,'setForSummer_app/map.html',{
        'lat':map.lat,
        'lng':map.lon,
    })

# Create your views here.
