from rest_framework import generics
from . import models, serializers


class CommentCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        photo_id = self.kwargs['photo_pk']
        return models.Comment.objects.filter(img_id=photo_id)

    def perform_create(self, serializer):
        photo_id = self.kwargs['photo_pk']
        photo = models.Photo.objects.get(pk=photo_id)
        serializer.save(user=self.request.user, img=photo)
