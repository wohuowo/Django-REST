#from django.db import router
from django.urls import path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
urlpatterns = [] + router.urls
#127.0.0.1:8000/posts