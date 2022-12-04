from django.views.generic import ListView

from things.models import Thing


class ThingListView(ListView):
    model = Thing
    template_name = 'things/home.html'
    context_object_name = 'things'

    # def get_queryset(self):
    #     return Thing.objects.filter(user=self.request.user)