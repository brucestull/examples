from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('things', views.ThingViewSet, basename='things')
router.register('users', views.UserViewSet, basename='users')
router.register('users-with-things', views.UserWithThingsViewSet, basename='users-with-things')
router.register('current-user', views.CurrentUserViewSet, basename='current-user')

urlpatterns = router.urls