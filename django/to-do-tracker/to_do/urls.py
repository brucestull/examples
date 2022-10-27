from django.urls import path

from . import views


app_name = 'to_do_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('toggle-complete/<int:pk>/', views.toggle_complete, name='toggle_complete'),
]