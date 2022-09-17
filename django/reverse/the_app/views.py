from django.shortcuts import render
from django.urls import reverse


def index(request):
    the_returned_object_of_reverse = reverse('the_app:index')
    print('The "reverse" function returns this URL-type string: ', the_returned_object_of_reverse)
    return render(request, 'index.html')
