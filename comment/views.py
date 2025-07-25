from rest_framework import generics
from . import models, serializers
from photo.models import Photo


class CommentCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    pagination_class = None

    def get_queryset(self):
        photo_id = self.kwargs['photo_pk']
        return models.Comment.objects.filter(photo_id=photo_id)

    def perform_create(self, serializer):
        photo_id = self.kwargs['photo_pk']
        photo = Photo.objects.get(pk=photo_id)
        serializer.save(user=self.request.user, photo=photo)
