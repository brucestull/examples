from django.http import HttpResponse
from django.shortcuts import render

from . import models


def simple_view_function(request):
    return HttpResponse("A hard-coded string to display on webpage!")


def show_all_things_view_function(request):
    all_the_things = models.TheThing.objects.all()
    context = {
        'all_things_context_variable_from_view_to_template': all_the_things,
    }
    return render(request,'the_things.html', context)