from django.views.generic import ListView
from django.contrib.auth import get_user_model

import pprint

from .models import Thing


class ThingAndUserListView(ListView):
    template_name = 'home.html'
    # The default context object name, derived from the model in 'get_queryset', is 'thing_list'.
    # The default 'general' context_object_name is 'object_list'.
    # context_object_name = 'things'

    def get_queryset(self):
        return Thing.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # pprint.pprint(context)
        print()
        print("Before we add our 'users' object : ")
        print()
        print('context.keys(): ', context.keys())
        
        context['users'] = get_user_model().objects.all()

        # pprint.pprint(context)
        print()
        print("After we add our 'users' object: ")
        print()
        print('context.keys(): ', context.keys())
        print()

        return context
