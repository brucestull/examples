from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def add(request):
    specific_to_do = request.POST.get('todo-from-template')
    print('specific_to_do: ', specific_to_do)
    return HttpResponseRedirect(reverse('home'))
