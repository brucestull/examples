from django.views.generic import ListView
from django.contrib.auth import get_user_model


class UsersWithThingsListView(ListView):
    model = get_user_model()
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print()
        print('context.keys(): ', context.keys())
        print()
        
        return context
