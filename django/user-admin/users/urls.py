from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/edit/', views.UserEditView.as_view(), name='edit_user')
]