from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'groups', views.GroupViewSet, basename='groups')

urlpatterns = router.urls + [

]

