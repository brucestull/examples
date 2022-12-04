from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'
router = DefaultRouter()
router.register('a-things', views.AThingViewSet, basename='a-things')

urlpatterns = router.urls + [

]