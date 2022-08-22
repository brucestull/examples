from django.http import HttpResponse
from .models import StringValue
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views import generic


class ClassListView(generic.ListView):
    """
    Class-based view using `ListView`.
    """
    model = StringValue
    context_object_name = 'the_string_things'
    template_name = 'the_app/the_app_template.html'


class ClassTemplateView(TemplateView):
    """
    Class-based view using `TemplateView`.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_string_values = StringValue.objects.all()
        context['the_string_things'] = the_string_values
        return context


class ClassView(View):
    """
    Class-based view using `View`.
    """
    def get(self, request):
        the_string_values = StringValue.objects.all()
        context = {
            'the_string_things': the_string_values
        }
        return render(request, 'the_app/the_app_template.html', context)


def function_view(request):
    """
    Function-based view to show a list view of model `StringValue`.
    """
    the_string_values = StringValue.objects.all()
    context = {
        'the_string_things': the_string_values
    }
    return render(request, 'the_app/the_app_template.html', context)


def index(request):
    """
    Basic Django index view to demonstrate a basic `HttpResponse` return of a string.
    """
    response_string = "Looks like we might have successful request-response!"
    return HttpResponse(response_string)

