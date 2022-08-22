from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, View

# It seems either of these imports will work.
    # from django.views.generic import ListView
    # from django.views.generic.list import ListView
from django.views.generic import ListView

from .models import StringValue


def index(request):
    """
    Basic Django index view to demonstrate a basic `HttpResponse` return of a string.
    """
    response_string = "Looks like we might have successful request-response!"
    return HttpResponse(response_string)


def function_view(request):
    """
    Function-based view to show a list view of model `StringValue`.
    """
    the_string_values = StringValue.objects.all()
    context = {
        'the_string_things': the_string_values
    }
    return render(request, 'the_app/the_app_template.html', context)


class ClassView(View):
    """
    Class-based view, which inherits from `django.views.generic.base.View` or `django.views.View`, to provide list view of model `StringValue`.
    """
    def get(self, request):
        the_string_values = StringValue.objects.all()
        context = {
            'the_string_things': the_string_values
        }
        return render(request, 'the_app/the_app_template.html', context)


class ClassTemplateView(TemplateView):
    """
    Class-based view, which inherits from `django.views.generic.base.TemplateView`, to provide list view of model `StringValue`.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        the_string_values = StringValue.objects.all()
        context['the_string_things'] = the_string_values
        return context


class ClassListView(ListView):
    """
    Class-based view, which inherits from `django.views.generic.ListView`, to provide list view of model `StringValue`.
    """
    model = StringValue
    context_object_name = 'the_string_things'
    template_name = 'the_app/the_app_template.html'

