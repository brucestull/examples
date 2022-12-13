from django.urls import path

from . import views


app_name = 'things'
urlpatterns = [
    path('', views.UsersWithThingsListView.as_view() , name='home'),
]