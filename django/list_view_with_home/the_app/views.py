from django.http import HttpResponse
from django.shortcuts import render

from .models import AwesomeCat


def home(request):
    queryset_of_awesome_cats = AwesomeCat.objects.all()
    context = {
        'view_to_template_object': queryset_of_awesome_cats
        }
    return render(request, 'the_app/home.html', context)

