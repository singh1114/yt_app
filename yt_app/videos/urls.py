from django.urls import path

from videos.views import (
    VideoDetailAPIView,
    VideoSearchAPIView
)

app_name = 'videos'


urlpatterns = [
    path('details', VideoDetailAPIView.as_view(),
         name='video_detail'),
    path('search/<str:query>', VideoSearchAPIView.as_view(),
         name='video_search'),
]
