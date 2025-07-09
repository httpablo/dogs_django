from django.urls import path
from . import views


urlpatterns = [
    path('photos/<int:photo_pk>/comments/', views.CommentCreateListAPIView.as_view(), name='photo-comments'),
]
