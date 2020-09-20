import arrow

from django.core.paginator import EmptyPage, Paginator
from django.db.models.query import QuerySet

from videos.models import VideoData


class VideoDataFormator:
    def format_video_data_list(
            self, video_list: QuerySet, page: int, limit: int) -> list:
        video_list = self.paginate_objects(video_list, page, limit)
        video_serialized_list = list()
        for video in video_list:
            video_serialized_list.append(self.format_video_data(video))

        return video_serialized_list

    @staticmethod
    def format_video_data(video_data: VideoData) -> dict:
        return {
            'uuid': video_data.uuid,
            'video_id': video_data.video_id,
            'title': video_data.title,
            'description': video_data.description,
            'published_at': video_data.published_at
        }

    @staticmethod
    def paginate_objects(db_queryset: QuerySet, page: int, limit: int):
        paginator = Paginator(db_queryset, limit)
        try:
            queryset = paginator.page(page)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        return queryset
