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
    user_current_todos = models.ToDo.objects.filter(person=current_user)
    current_priorities_for_form = models.Priority.objects.all()
    context = {
        'todos': user_current_todos,
        'priorities': current_priorities_for_form,
    }
    return render(request, 'home.html', context)


@login_required
def add_priority(request):
    """
    Create a new `Priority` object from user's input then redirect to 'to_dos_app:index'.
    """
    if request.method == 'POST':
        new_priority_description = request.POST.get('priority-description-from-form')
        new_priority_level = request.POST.get('priority-level-from-form')

        if new_priority_description != '' and new_priority_level != '':
            new_priority = models.Priority.objects.create(
                description=new_priority_description,
                priority_level=new_priority_level,
            )

            ###############################################################
            # Print Statements
            print("We're adding a Priority?!")
            the_keys = request.POST.keys()
            print('the_keys: ', the_keys)
            # the_keys:  dict_keys([
            #     'csrfmiddlewaretoken',
            #     'priority-description-from-form',
            #     'priority-level-from-form'
            # ])
            print('new_priority_description: ', new_priority_description)
            print('new_priority_level: ', new_priority_level)
            print('new_priority: ', new_priority)
            print("New Priority created!")
            ###############################################################

        else:
            print("No new Priority created since user provided no values in form!")

    else:
        print("No new Priority created since request is GET method!")

    return HttpResponseRedirect(reverse('to_dos_app:index'))


@login_required
def add_todo(request):
    """
    Create a new `ToDo` from user's description and `Priority` choice.
    """
    if request.method == 'POST':
        new_todo_description = request.POST.get('todo-description-from-form')
        new_todo_user = request.user

        ###############################################################
        # Print Statements
        print('request.user: ', request.user)
        ###############################################################

        if new_todo_description != '':
            new_todo_priority_id  = request.POST.get('priority-id-from-form')
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
            print('ToDo not created since no user input?!')
            ###############################################################

    else:
        print("No new ToDo created since request is GET method!")

    return HttpResponseRedirect(reverse('to_dos_app:index'))


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
        print("Current Completion status: ", current_todo.completed)
        print("We're toggling the ToDo...: ", current_todo)
        ###############################################################
    
        if current_todo.completed:
            current_todo.completed = False
            current_todo.completed_date = None
        else:
            current_todo.completed = True
            current_todo.completed_date = timezone.now()
        current_todo.save()

        ###############################################################
        # Print Statements
        print("New Completion status: ", current_todo.completed)
        ###############################################################

    return HttpResponseRedirect(reverse('to_dos_app:index'))


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
    return HttpResponseRedirect(reverse('to_dos_app:index'))
