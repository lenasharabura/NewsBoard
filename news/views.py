from django.http import Http404
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import Post, Comment
from news.permissions import IsOwnerOrReadOnly
from news.serializers import PostSerializer, CommentSerializer

__all__ = [
    'PostsListView',
    'PostDetailView',
    'PostUpvoteView',
    'CommentListView',
    'CommentDetailView',
]


class PostsListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsOwnerOrReadOnly]


class PostUpvoteView(APIView):
    allowed_methods = ['POST']
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        post_id = self.kwargs["post_id"]
        post_votes_id = Post.objects.filter(id=post_id).prefetch_related('amount_of_upvotes')

        if request.user not in post_votes_id.first().amount_of_upvotes.all():
            post_votes_id.first().amount_of_upvotes.add(request.user)
            return Response({"detail": "Success"}, status=status.HTTP_200_OK)
        return Response(
            {"detail": "You cannot upvote twice"},
            status=status.HTTP_400_BAD_REQUEST
        )


class CommentListView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        try:
            return Comment.objects.filter(post_id=post_id)
        except Comment.DoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user, post_id=self.kwargs.get("post_id"))


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsOwnerOrReadOnly]
