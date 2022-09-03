from django.shortcuts import render
from django.http import HttpResponse

from .models import AwesomeCat


def index_view(request):
    """
    Simple `index_view` method that renders the `AwesomeCat` list template.
    """
    awesome_cat_objects = AwesomeCat.objects.all()
    print(awesome_cat_objects)
    context = {
        'view_to_template_objects': awesome_cat_objects
    }
    return render(request, 'the_app/index_template.html', context)


def create(request):

    # print('type(request): ', type(request))
    # print('request: ', request)
    # print('type(request.POST): ', type(request.POST))
    print('request.POST: ', request.POST)

    console_string = "Create view, ACTIVATED! ...CONSOLE!"
    # print(console_string)
    web_response_string = "Create view, ACTIVATED! ...BROWSER!"
    return HttpResponse(web_response_string)