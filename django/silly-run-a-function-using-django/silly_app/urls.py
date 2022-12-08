from django.urls import path

from . import views


urlpatterns = [
    path(
        'url-for-silly-view/',
        views.silly_view,
        name='silly-view-name',
    )
]
