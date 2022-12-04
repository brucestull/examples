from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()
router.register('things', views.ThingViewSet, basename='things')

urlpatterns = router.urls + [

]