from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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
            # logout(request)
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


def edit(request):
    """
    Function-based view to display edit `User` form on `GET` request,
    and change `User` on `POST` request.
    """
    print('request.user: ', request.user)
    if request.method == 'POST':
        username_in_view = request.POST.get('username_in_form')
        if username_in_view != '' and request.user.username != username_in_view:
            print("WOMP WOMP!!! Tricksie Hobbitses!!")
            context = {
                'message': "Editing user information that are not you is forbidden!"
            }
            return render(request, 'registration/edit.html', context)

        current_user = get_object_or_404(User, username=username_in_view)
        print("We got a legit USER!!!")
        print('current_user: ', current_user)
        
        password_in_view = request.POST.get('password_in_form')
        password_confirm_in_view = request.POST.get('password_confirm_in_form')
        print('POST!!!')
        return HttpResponseRedirect(reverse('the_users_app:home'))

    return render(request, 'registration/edit.html')
    