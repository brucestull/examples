from django.urls import path

from . import views


app_name = 'to_dos_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-priority/', views.add_priority, name='add_priority'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('toggle-complete/<int:pk>/', views.toggle_complete, name='toggle_complete'),
]