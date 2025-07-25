from rest_framework import generics
from . import models, serializers, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import F


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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.accesses = F('accesses') + 1
        instance.save(update_fields=['accesses'])
        instance.refresh_from_db()

        return super().retrieve(request, *args, **kwargs)


class UserStatsAPIView(APIView):
    def get(self, request):
        user = request.user
        photos = models.Photo.objects.filter(user=user)
        serializer = serializers.PhotoSerializer(photos, many=True)

        return Response(serializer.data)
