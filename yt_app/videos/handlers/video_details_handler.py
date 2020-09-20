import arrow

from videos.models import VideoData

from videos.handlers.video_data_utils import VideoDataFormator


class VideoDetailHandler:
    def get_video_handler(self, page: int, limit: int) -> list:
        videos = VideoData.objects.all()
        return VideoDataFormator().format_video_data_list(videos, page, limit)
