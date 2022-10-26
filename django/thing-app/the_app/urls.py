from django.urls import path

from . import views


app_name = 'our_app_name'

urlpatterns = [
    path('url-fragment-for-simple-view-function/', views.simple_view_function, name='simple_view_name'),
]