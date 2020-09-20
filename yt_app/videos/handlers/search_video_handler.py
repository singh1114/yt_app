from django.db.models import Q

from videos.models import VideoData
from videos.handlers.video_data_utils import VideoDataFormator


class SearchVideoHandler:
    def search_videos(self, query: str, page: int, limit: int) -> list:
        print("query: " + query)
        video_queryset = VideoData.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return VideoDataFormator().format_video_data_list(
            video_queryset, page, limit)
