from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TodoViewSet


router = DefaultRouter()
router.register('', TodoViewSet, basename='todos')
urlpatterns = [
    
] + router.urls



# #### Alternate code for TodoViewSet ####
# from .views import TodoList, TodoDetail

# urlpatterns = [
#     path('', TodoList.as_view()),
#     path('<int:pk>/', TodoDetail.as_view()),
# ]
# ########################################