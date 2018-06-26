from django.shortcuts import render, redirect, HttpResponse


def setHome(request):
    # return HttpResponse('you made it home')
    return render(request, 'setForSummer_app/index.html')

def food(request):
    return render(request, 'setForSummer_app/food.html')

# Create your views here.
