from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

from .models import User

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        print('request.POST: ', request.POST)
        form =  NewUserForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            print('username: ', username)
            raw_password = form.cleaned_data.get('password1')
            print('raw_password: ', raw_password)
            email = form.cleaned_data.get('email')
            print('email: ', email)

            user = authenticate(username=username, password=raw_password, email=email)
            print('User.objects.all() after authenticate(): ', User.objects.all())
            print('user: ', user)
            the_form = form.save()
            print('User.objects.all() after form.save(): ', User.objects.all())
            print('the_form: ', the_form)
            print('type(the_form): ', type(the_form))
            login(request, user)

            return redirect('index')
    else:
        form = NewUserForm()
    return render(request, 'registration/register.html', {'form': form})