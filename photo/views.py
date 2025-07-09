from rest_framework import generics
from . import models, serializers, permissions


class PhotoCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly]
