from django.views.generic import ListView

from .models import Thing


class ThingListView(ListView):
    model = Thing
    template_name = 'things/things_list.html'

    def get_queryset(self):
        return Thing.objects.all().filter(name__contains='car')
