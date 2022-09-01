from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    the_return_string = 'Goodbuy, World! Enjoy the sail!'
    return HttpResponse(the_return_string)
