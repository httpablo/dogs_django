from rest_framework import generics
from . import models, serializers, permissions


class PhotoCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_param = self.request.query_params.get('user')

        if user_param and user_param != '0':
            queryset = queryset.filter(user__username=user_param)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly]
