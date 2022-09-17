from django.urls import path

from . import views


app_name = 'the_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/complete/', views.complete, name='complete'),
    path('<int:pk>/un-complete/', views.uncomplete, name='uncomplete'),
]
