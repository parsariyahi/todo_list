from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import Todo

# Create your views here.
#/usr/accounts/login/

@login_required(login_url='/usr/accounts/login/')
def index(request):
    todos = Todo.objects.filter(owner=request.user)
    context = {'todos': todos}

    return render(request, 'todos/index.html', context)

@login_required(login_url='/usr/accounts/login/')
def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    return render(request, 'todos/detail.html', {'todo': todo})

@login_required(login_url='/usr/accounts/login/')
def create(request):
    if request.method == 'POST':
        if request.POST.get('create_todo', False) :
            data = {
                'owner': request.user,
                'name': request.POST.get('name'),
                'description': request.POST.get('description'),
                'pub_date': date.today()
            }
            new_todo = Todo(**data)
            new_todo.save()

            return HttpResponseRedirect(reverse('todos:index'))

    return render(request, 'todos/index.html')


@login_required(login_url='/usr/accounts/login/')
def done(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('todos:index'))
