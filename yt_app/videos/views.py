from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from videos.handlers.video_details_handler import VideoDetailHandler
from videos.handlers.search_video_handler import SearchVideoHandler


class VideoDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        page: int = request.GET.get('page', 1)
        limit: int = request.GET.get('limit', 10)
        data = VideoDetailHandler().get_video_handler(page, limit)
        return Response(status=status.HTTP_200_OK, data=data)


class VideoSearchAPIView(APIView):
    def get(self, request, query, *args, **kwargs):
        page: int = request.GET.get('page', 1)
        limit: int = request.GET.get('limit', 10)
        data = SearchVideoHandler().search_videos(query, page, limit)
        return Response(status=status.HTTP_200_OK, data=data)
