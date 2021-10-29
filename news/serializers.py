from rest_framework import serializers

from news.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(read_only=True)
    amount_of_upvotes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_amount_of_upvotes(self, obj):
        return obj.amount_of_upvotes.count()


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(read_only=True)
    post = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
