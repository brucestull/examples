from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

from . import models


def index(request):
    the_todos = models.ToDo.objects.filter(completed_date=None)
    # print('the_todos: ', the_todos)
    the_todones = models.ToDo.objects.exclude(completed_date=None)
    # print('the_todones: ', the_todones)x
    the_priorities = models.Priority.objects.all()
    context = {
        'the_priorities': the_priorities,
        'the_todos': the_todos,
        'the_todones': the_todones,
    }
    return render(request, 'index.html', context)

def create(request):
    the_request_stuff_we_need = request.POST
    # print(the_request_stuff_we_need)

    todo_text = the_request_stuff_we_need.get('the_todo_text')
    # print(todo_text)

    todo_priority_id = the_request_stuff_we_need.get('the_priority_chosen')
    priority_of_new_todo = get_object_or_404(models.Priority, pk=todo_priority_id)

    if the_request_stuff_we_need.get('the_todo_text') == '':
        return HttpResponseRedirect(reverse('the_app:index'))

    the_new_todo = models.ToDo.objects.create(text=todo_text, priority=priority_of_new_todo)
    # print(the_new_todo)
    return HttpResponseRedirect(reverse('the_app:index'))

def complete(request, pk):
    the_todo_we_want_to_complete = get_object_or_404(models.ToDo, id=pk)
    totally_now = datetime.datetime.now()
    the_todo_we_want_to_complete.completed_date = totally_now
    the_todo_we_want_to_complete.save()
    # print('totally_now: ', totally_now)
    # print('type(totally_now): ', type(totally_now))
    # print('the_todo_we_want_to_complete: ', the_todo_we_want_to_complete)
    # print('type(the_todo_we_want_to_complete): ', type(the_todo_we_want_to_complete))
    # type(the_todo_we_want_to_complete):  <class 'the_app.models.ToDo'>
    # the_request_stuff_we_need = request.POST
    # print(the_request_stuff_we_need)
    # print('type(the_request_stuff_we_need): ', type(the_request_stuff_we_need))
    return HttpResponseRedirect(reverse('the_app:index'))

def uncomplete(request, pk):
    the_todo_we_want_to_un_complete = get_object_or_404(models.ToDo, id=pk)
    the_todo_we_want_to_un_complete.completed_date = None
    the_todo_we_want_to_un_complete.save()
    return HttpResponseRedirect(reverse('the_app:index'))