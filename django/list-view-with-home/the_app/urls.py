from django.urls import path

from . import views


app_name = 'the_app'
urlpatterns = [
    path('home/', views.home, name='home'),
]