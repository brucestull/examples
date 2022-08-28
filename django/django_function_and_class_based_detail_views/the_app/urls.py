from django.urls import path
from . import views
from django.views.generic.base import TemplateView


app_name = 'app_name_in_html'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('function-view/', views.function_list_view, name='function_list_view'),
    path('class-view/', views.ClassView.as_view(), name='class_view'),
    path(
        'class-template-view/',
        views.ClassTemplateView.as_view(
            template_name='the_app/the_app_template.html'
        ),
        name='class_template_view'
    ),
    path('class-list-view/', views.ClassListView.as_view(), name='class_list_view'),
]