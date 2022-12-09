from django.urls import path

from .views import ThingListView


app_name = 'things'

urlpatterns = [
    path('', ThingListView.as_view(), name='list'),
]