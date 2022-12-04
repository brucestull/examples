from django.urls import path
from django.views.generic.base import TemplateView

from . import views


app_name = 'the_django_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='django_app/home.html'), name='home'),
    path('a-things/', views.AThingListView.as_view(), name='a-things'),
]
