from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.ManyToManyField(User, related_name='posts_vote', blank=True)
    author_name = models.ForeignKey(User, related_name='authors', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:25]
