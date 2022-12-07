from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.UserListView.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/edit/', views.UserEditView.as_view(), name='edit_user'),
    path('<int:pk>/whatever/', views.WhateverCanView.as_view(), name='whatever'),
    path('<int:pk>/recruiter/', views.RecruiterCanView.as_view(), name='recruiter'),
]