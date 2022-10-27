from django.urls import path

from . import views


app_name = 'to_do_app'

urlpatterns = [
    path('add/', views.add, name='add'),
]