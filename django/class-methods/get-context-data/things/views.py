from django.views.generic import ListView

from .models import Thing


class ThingListView(ListView):
    model = Thing
    template_name = 'things/things_list.html'

    def get_context_data(self, **kwargs):
        """
        We do `super().get_context_data(**kwargs)` so we can get the
        stuff Django needs to get and then we will add our stuff to that `context`.
        """
        # Populate `object_list` with the queryset.
        context = super().get_context_data(**kwargs)
        # Populate `context` with our `things` stuff.
        context['things'] = self.get_queryset()
        # Populate `context` with our `computers` stuff.
        context['computers'] = self.get_queryset().filter(name__contains='computer')
        # Populate `context` with our `cars` stuff.
        context['cars'] = self.get_queryset().filter(name__contains='car')
        return context