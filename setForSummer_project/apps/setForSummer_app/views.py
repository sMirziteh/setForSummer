from django.shortcuts import render, redirect, HttpResponse


def setHome(request):
    # return HttpResponse('you made it home')
    return render(request, 'setForSummer_app/index.html')

def food(request):
    return render(request, 'setForSummer_app/food.html')

def activities(request):
    return render(request, 'setForSummer_app/activities.html')

def learning(request):
    return render(request, 'setForSummer_app/learning.html')

def faqs(request):
    return render(request, 'setForSummer_app/faqs.html')

def contact(request):
    return render(request, 'setForSummer_app/contact.html')

# Create your views here.
