from rest_framework import serializers
from photo.models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Photo
        fields = ['id', 'user', 'name', 'weight', 'age', 'img', 'accesses', 'created_at', 'update_at']
