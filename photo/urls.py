from django.urls import path
from . import views


urlpatterns = [
    path('photos/', views.PhotoCreateListAPIView.as_view(), name='photo_create_list_api_view'),
    path('photo/<int:pk>/', views.PhotoRetrieveUpdateDestroyAPIView.as_view(), name='photo_detail_api_view'),
    path('stats/', views.UserStatsAPIView.as_view(), name='user_stats_api_view'),
]
