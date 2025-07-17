from django.urls import path
from . import views


urlpatterns = [
    path('photos/', views.PhotoCreateListAPIView.as_view(), name='photo-create-list-api-view'),
    path('photo/<int:pk>/', views.PhotoRetrieveUpdateDestroyAPIView.as_view(), name='photo-detail-api-view'),
]
