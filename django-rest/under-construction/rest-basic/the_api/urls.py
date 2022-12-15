from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'users-api-url', views.UserViewSet, basename='users_url_namespace')
router.register('groups-api-url', views.GroupViewSet, basename='groups_url_namespace')

urlpatterns = router.urls + [

]

