from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from . import models


@login_required
def index(request):
    """
    Get the `ToDo` and `Priority` objects from the database and render
    them in the `home.html` template.
    """
    current_user = request.user
    current_todos = models.ToDo.objects.filter(person=current_user)
    # current_todos = models.ToDo.objects.all()
    current_priorities = models.Priority.objects.all()
    context = {
        'todos': current_todos,
        'priorities': current_priorities,
    }
    return render(request, 'home.html', context)


def add(request):
    """
    Create a new `ToDo` from user's description and `Priority` choice.
    """
    new_todo_description = request.POST.get('todo_text-from-template')
    new_todo_user = request.user

    ###############################################################
    # Print Statements
    print('request.user: ', request.user)
    ###############################################################

    if new_todo_description != '':
        new_todo_priority_id  = request.POST.get('priority-id-from-template')
        new_todo_priority = get_object_or_404(
            models.Priority,
            id=new_todo_priority_id
        )
        new_todo = models.ToDo.objects.create(
            description=new_todo_description,
            priority=new_todo_priority,
            person=new_todo_user,
        )
    
        ###############################################################
        # Print Statements
        print('new_todo_description: ', f"'{new_todo_description}'")
        print('new_todo_priority_id: ', new_todo_priority_id)
        print('new_todo_priority: ', new_todo_priority)
        print('New ToDo added: ', new_todo)
        ###############################################################

    else:

        ###############################################################
        # Print Statements
        print('ToDo not created.')
        ###############################################################

    return HttpResponseRedirect(reverse('to_do_app:index'))


def toggle_complete(request, pk):
    """
    Toggle the `ToDo` with the given `pk` between `complete` and `incomplete`.
    """
    current_todo = get_object_or_404(models.ToDo, pk=pk)
    current_user = request.user
    if current_user == current_todo.person:
    
        ###############################################################
        # Print Statements
        print('current_user: ', current_user)
        print("We're toggling the ToDo...: ", current_todo)
        ###############################################################
    
        if current_todo.completed:
            current_todo.completed = False
            current_todo.completed_date = None
        else:
            current_todo.completed = True
            current_todo.completed_date = timezone.now()
        current_todo.save()
    return HttpResponseRedirect(reverse('to_do_app:index'))


def delete(request, pk):
    """
    Delete the `ToDo` with the given `pk`.
    """
    current_todo = get_object_or_404(models.ToDo, pk=pk)
    current_user = request.user
    if current_user == current_todo.person:
        ###############################################################
        # Print Statements
        print('current_user: ', current_user)
        print("We're deleting the ToDo...: ", current_todo)
        ###############################################################
    
        current_todo.delete()
    return HttpResponseRedirect(reverse('to_do_app:index'))
