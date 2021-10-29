from django.urls import path
from news.views import *

urlpatterns = [
    # Posts
    path('posts/', PostsListView.as_view(), name='posts_list'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    # Upvote
    path('posts/<int:post_id>/upvote/', PostUpvoteView.as_view(), name='post_upvote'),
    # Comments
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comments_list'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', CommentDetailView.as_view(), name='comment_detail'),

]
