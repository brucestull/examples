from django.urls import path

from .views import SignUpView, UserListView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/', UserListView.as_view(), name='user_list'),
]