from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import NoChoices, YesChoices



def index(request):
    return_string = "Welcome, to... The Machine!</br>Can you see me now?"
    return HttpResponse(return_string)


class NoChoicesListView(ListView):
    """
    ListView for the model `NoChoices`.
    """
    model = NoChoices
    """
    # `ListView` properties:
    #     Defaults:
    #         template_name = `objectname_list.html`
    #         context_object_name = `object_list`
    """


class YesChoicesListView(ListView):
    """
    ListView for the model `YesChoices`.
    """
    model = YesChoices
    """
    # `ListView` properties:
    #     Defaults:
    #         template_name = `objectname_list.html`
    #         context_object_name = `object_list`
    """


class YesChoicesCreateView(CreateView):
    model = YesChoices
    fields = ['name', 'the_specific_choice']


class NoChoicesCreateView(CreateView):
    model = NoChoices
    fields = ['name']
