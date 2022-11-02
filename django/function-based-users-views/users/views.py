from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in_the_user


def login(request):
    if request.method == 'POST':

        print("We gotta 'POST' request!!!")
        print("Do the login logic here!")

        username_in_view = request.POST.get('username_in_form')
        password_in_view = request.POST.get('password_in_form')
        print('username_in_view: ', username_in_view)
        print('password_in_view: ', password_in_view)

        # Returns a 'user' if they can be authenticated, otherwise, returns 'None'.
        # This does NOT seem to log the user in.
        user = authenticate(username=username_in_view, password=password_in_view)
        print('user: ', user)
        if user is not None:
            print(user, ": 'user' IS authenticated!")
            print('Log in user: ', user)
            log_in_the_user(request, user)
        else:
            print(user, ": 'user' IS NOT authenticated!")

        print("Redirect the user to some other view after login logic. This creates a new 'request'.")
        return HttpResponseRedirect(reverse('the_users_app:home'))

    print("It's obviously a 'GET' request!")

    return render(request, 'registration/login.html')