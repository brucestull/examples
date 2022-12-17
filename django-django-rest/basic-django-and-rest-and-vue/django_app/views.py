from django.views.generic import ListView

from .models import AThing


class AThingListView(ListView):
    model = AThing
    context_object_name = 'things'
    template_name = 'django_app/home.html'