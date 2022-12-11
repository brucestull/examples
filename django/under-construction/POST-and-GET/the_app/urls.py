from django.urls import path

from . import views


app_name = 'the_app_name'

urlpatterns = [
    path(
        'index-view-route/',
        views.index,
        name='index_view_name'
    ),
]
