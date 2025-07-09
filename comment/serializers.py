from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    img = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'img', 'comment', 'created_at',]
