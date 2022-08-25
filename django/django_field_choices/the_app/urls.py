from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('no-choices/',
        views.NoChoicesListView.as_view(),
        name='no-choices-view'
        ),
    path('yes-choices/',
        views.YesChoicesListView.as_view(),
        name='yes-choices-view'
        ),
]
