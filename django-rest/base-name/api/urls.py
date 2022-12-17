from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('things', views.ThingViewSet, basename='the-thing-api-viewname')
router.register('users', views.UserViewSet, basename='the-user-api-viewname')
router.register('current-user-list', views.CurrentUserViewSet, basename='the-current-user-list-api-viewname')

urlpatterns = router.urls + [
    path('current-user/', views.CurrentUserView.as_view(), name='the-current-user-api-viewname'),
]