from django.shortcuts import render, redirect, HttpResponse


def setHome(request):
    # return HttpResponse('you made it home')
    return render(request, 'setForSummer_app/index.html')

# Create your views here.
