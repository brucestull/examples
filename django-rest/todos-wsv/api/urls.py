# from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.TodoViewSet, basename='todos')
urlpatterns = router.urls

# urlpatterns = [
#     path('', views.TodoList.as_view()),
#     path('<int:pk>/', views.TodoDetail.as_view()),
# ]