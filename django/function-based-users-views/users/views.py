from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in_the_user


def login(request):
    if request.method == 'POST':
        username_in_view = request.POST.get('username_in_form')
        password_in_view = request.POST.get('password_in_form')
        user = authenticate(username=username_in_view, password=password_in_view)
        if user is not None:
            log_in_the_user(request, user)
        return HttpResponseRedirect(reverse('the_users_app:home'))

    return render(request, 'registration/login.html')