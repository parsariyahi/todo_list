from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}

    return render(request, 'todos/index.html', context)

def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    return render(request, 'todos/detail.html', {'todo': todo})

def create(request):
    if request.method == 'POST':
        if request.POST.get('create_todo', False) :
            data = {
                'name': request.POST.get('name'),
                'description': request.POST.get('description'),
                'pub_date': date.today()
            }
            new_todo = Todo(**data)
            new_todo.save()

            return HttpResponseRedirect(reverse('todos:index'))

    return render(request, 'todos/create.html')