from django.views.generic import ListView
from django.contrib.auth import get_user_model

from .models import Thing


class ThingAndUserListView(ListView):
    template_name = 'home.html'
    context_object_name = 'things'

    def get_queryset(self):
        return Thing.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all()
        print(context)
        return context
