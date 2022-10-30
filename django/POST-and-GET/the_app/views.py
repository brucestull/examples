from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        print('request.method: ', request.method)
        print("Do 'POST' logic here.")
        # Use `HttpResponseRedirect` so user does not submit same form
        #     multiple times.
        return HttpResponseRedirect(reverse('the_app_name:index_view_name'))
    # If request.method is not `POST` it will probably be `GET`.
    else:
        print('request.method: ', request.method)
        print("Do 'GET' logic here.")
        return render(request, 'home.html')
