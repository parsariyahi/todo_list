from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import Todo

#/usr/accounts/login/
LOGIN_URL='/usr/accounts/login/'

@login_required(login_url=LOGIN_URL)
def index(request):
    """
    render the main todo page,
    login is required.

    :return
        :render todos/index
    """
    todos = Todo.objects.filter(owner=request.user) #returns the user's todos
    context = {'todos': todos}

    return render(request, 'todos/index.html', context)

@login_required(login_url=LOGIN_URL)
def detail(request, todo_id):
    """
    show the detail of each todo by their id,
    login is required.

    :param todo_id Type[int] 
    :return
        :render todos/detail
    """
    todo = get_object_or_404(Todo, pk=todo_id)

    return render(request, 'todos/detail.html', {'todo': todo})

@login_required(login_url=LOGIN_URL)
def create(request):
    """
    create a todo,
    login is required.

    :return
        :redirect todos/index
        :render todos/index
    """
    if request.method == 'POST':
        if request.POST.get('create_todo', False) : #if the form was submited
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


@login_required(login_url=LOGIN_URL)
def done(request, todo_id):
    """
    delete a todo (means its done),
    login is required.

    :return
        :redirect todos/index
    """
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect(reverse('todos:index'))
