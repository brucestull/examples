from django.urls import path

from . import views


app_name = 'things'
urlpatterns = [
    path('', views.ThingAndUserListView.as_view(), name='home'),
]