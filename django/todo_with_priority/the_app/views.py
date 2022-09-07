from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import models


def index(request):
    the_todos = models.ToDo.objects.all()
    the_priorities = models.Priority.objects.all()
    context = {
        'the_priorities': the_priorities,
        'the_todos': the_todos,
    }
    return render(request, 'index.html', context)

def create(request):
    the_request_stuff_we_need = request.POST
    print(the_request_stuff_we_need)

    todo_text = the_request_stuff_we_need.get('the_todo_text')
    print(todo_text)

    todo_priority_id = the_request_stuff_we_need.get('the_priority_chosen')
    priority_of_new_todo = get_object_or_404(models.Priority, pk=todo_priority_id)

    if the_request_stuff_we_need.get('the_todo_text') == '':
        return HttpResponseRedirect(reverse('the_app:index'))

    the_new_todo = models.ToDo.objects.create(text=todo_text, priority=priority_of_new_todo)
    print(the_new_todo)
    return HttpResponseRedirect(reverse('the_app:index'))