from django.urls import path
from . import views


app_name = 'the_app'
urlpatterns = [
    path('index-url/', views.index_view, name='index_named_url')
]

