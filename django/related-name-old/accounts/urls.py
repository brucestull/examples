from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('current-user/', views.CurrentUserView.as_view(), name='current_user'),
]