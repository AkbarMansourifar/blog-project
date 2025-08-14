from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer 

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)  # فقط QuerySet برمیگردونه

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(user=self.request.user, post_id=post_id)  # ذخیره رکورد جدید اینجا انجام میشه
