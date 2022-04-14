from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from todos.models import Todo

# Create your views here.
@login_required(login_url='/usr/accounts/login/')
def dashboard(request):
    """
    render the main dahsboard page,
    login is required.

    :return
        :render dashboard/index
    """
    todos = Todo.objects.filter(owner=request.user)
    context = {'todos': todos}

    return render(request, 'dashboard/index.html', context)


def register(request):
    """
    create new user

    :return
        :redirect usr/dash
        :render registration/register
    """
    if request.method == 'POST' :
        if request.POST.get('register', '') :
            new_user = {
                'username':request.POST.get('username'),
                'email': request.POST.get('email'),
                'password': request.POST.get('password1'),
            }
            password2 = request.POST.get('password2')
            if new_user['password'] == password2 :
                user = User.objects.create_user(**new_user)
                login(request, user)
                return redirect('/usr/dash')
        
    return render(request, 'registration/register.html')