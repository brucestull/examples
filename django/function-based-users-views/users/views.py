from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in_the_user
from django.contrib.auth import logout as log_out_the_user
from django.contrib.auth.models import User

from django.db import IntegrityError


def sign_up(request):
    if request.method == 'POST':
        username_in_view = request.POST.get('username_in_form')
        password_in_view = request.POST.get('password_in_form')
        password_confirm_in_view = request.POST.get('password_confirm_in_form')
        if password_in_view != password_confirm_in_view:
            message = 'Passwords do not match'
            context = {
                'message': message
            }
            return render(request, 'registration/signup.html', context)
        try:
            the_new_user = User.objects.create_user(
                username=username_in_view,
                password=password_in_view
            )
            return HttpResponseRedirect(reverse('the_users_app:login'))

        except IntegrityError as e:
            print('type(e): ', type(e))
            e.message = 'User already exists: ' + username_in_view
            context = {
                'message': e.message
            }
            return render(request, 'registration/signup.html', context)

        except ValueError as e:
            print('type(e): ', type(e))
            e.message = 'Please provide a username'
            context = {
                'message': e.message
            }
            return render(request, 'registration/signup.html', context)

    return render(request, 'registration/signup.html')


def login(request):
    """
    Function-based view to display the Login form on `GET` request,
    and attempt to log in the user on `POST` request.
    """
    if request.method == 'POST':
        username_in_view = request.POST.get('username_in_form')
        password_in_view = request.POST.get('password_in_form')
        user = authenticate(username=username_in_view, password=password_in_view)
        if user is not None:
            log_in_the_user(request, user)
        return HttpResponseRedirect(reverse('the_users_app:home'))

    return render(request, 'registration/login.html')


def logout(request):
    """
    Function-based view to log out the user on `POST` request.
    """
    log_out_the_user(request)
    return HttpResponseRedirect(reverse('the_users_app:home'))

