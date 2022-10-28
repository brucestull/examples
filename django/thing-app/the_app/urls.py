from django.urls import path

from . import views


app_name = 'our_app_name'

urlpatterns = [
    path(
        'url-route-for-simple-view-function/',
        views.simple_view_function,
        name='simple_view_name'
    ),
    path(
        'show-all-things-url/',
        views.show_all_things_view_function,
        name='show_all_things_view_name'
    ),
]