from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')


def processReg(request):
    print(request.POST)
    result = Users.objects.validateRegistration(request.POST)
    print(result)
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email'] = request.POST['email']
    if type(result) is list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = result.id
    return redirect(f'/success')


def login(request):
    result = Users.objects.validateLogin(request.POST)
    print(result)
    request.session['lemail'] = request.POST['lemail']
    if type(result) is str:
        messages.error(request, result)
        return redirect('/')
    else:
        request.session['user_id'] = result.id
    return redirect(f'/success')

# def success(request):
    
#     context = {
#         'user': Users.objects.get(id=request.session['user_id']),
        
#     }
#     return render(request, 'wall_app/index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')

