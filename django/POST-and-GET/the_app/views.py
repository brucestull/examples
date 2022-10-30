from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        print('request.method: ', request.method)
        return HttpResponseRedirect(reverse('the_app_name:index_view_name'))
    # If request.method is not `POST` it will probably be `GET`.
    else:
        print('request.method: ', request.method)
        return render(request, 'home.html')
