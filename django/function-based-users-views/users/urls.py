from django.urls import path
from django.views.generic.base import TemplateView

from . import views


app_name = 'the_users_app'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', views.login, name='login'),
]