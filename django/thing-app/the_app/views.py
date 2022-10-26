from django.http import HttpResponse

def simple_view_function(request):
    return HttpResponse("A hard-coded string to display on webpage!")
