from django.contrib import admin

from news.models import Comment, Post

admin.site.register(Comment)
admin.site.register(Post)
