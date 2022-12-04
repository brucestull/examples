from django.urls import path
from django.views.generic.base import TemplateView

from .views import ThingListView


app_name = 'things_app_name'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('vanilla-django-list-view', ThingListView.as_view(), name='vanilla-django-list-view'),
]