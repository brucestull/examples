from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views


app_name = 'api'

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('current-user', views.CurrentUserViewSet, basename='current-user')

urlpatterns = router.urls + [

]