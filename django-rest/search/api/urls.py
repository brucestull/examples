from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(
    'things',
    views.ThingViewSet,
    basename='the-thing-api-viewname'
)
router.register(
    'users',
    views.UserViewSet,
    basename='the-user-api-viewname'
)
router.register(
    'current-user-list',
    views.CurrentUserViewSet,
    basename='the-current-user-list-api-viewname'
)

urlpatterns = [
    path(
        'current-user/',
        views.CurrentUserView.as_view(),
        name='the-current-user-api-viewname'
    ),
    path(
        'users/username/',
        views.UserUsernameSearchView.as_view(),
        name='username-search'
    ),
    path(
        'things/description/',
        views.ThingDescriptionSearchView.as_view()
    ),
    path(
        'things/name/',
        views.ThingNameSearchView.as_view(),
        name='name-search'
    ),
    path(
        'things-github/name/',
        views.ThingGithubNameSearchView.as_view()
    ),
] + router.urls