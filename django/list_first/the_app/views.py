from django.shortcuts import render

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
    
