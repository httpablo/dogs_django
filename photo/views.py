from rest_framework import generics
from . import models, serializers, permissions


class PhotoCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer

    def get_queryset(self):
        """
        Sobrescreve o queryset para filtrar as fotos por usuário,
        se o parâmetro 'user' for passado na URL.
        """
        queryset = super().get_queryset()

        user_id = self.request.query_params.get('user')

        if user_id:
            queryset = queryset.filter(user__id=user_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly]
