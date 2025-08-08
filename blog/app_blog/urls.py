from django.urls import path
from .views import *


urlpatterns = [
    path('api/posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    ]
