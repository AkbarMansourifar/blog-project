from django.urls import path
from .views import CommentListCreateView

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    ]