import arrow
import requests

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status

from videos.constants import YOUTUBE_API_URL
from videos.models import VideoData


class VideoDataFetchHandler:
    api_key = "AIzaSyBeE012Vo5cfSLoB3Uox2iPJaUpxAlmqAk"
    query = "football"

    def fetch_and_insert_video_data(self) -> None:
        api_key = self.fetch_api_key()
        self.insert_yt_data_into_db(api_key)

    def fetch_api_key(self) -> str:
        return self.api_key

    def insert_yt_data_into_db(self, api_key: str) -> None:
        try:
            import ipdb; ipdb.set_trace()
            yt_data = self.fetch_youtube_api_response(api_key)
            if yt_data:
                self.get_or_create_yt_data(yt_data)
            else:
                print("No data from youtube api")
        except Exception as e:
            print(e)

    def fetch_youtube_api_response(self, api_key: str) -> dict:
        # TODO change this with the current date.
        url = YOUTUBE_API_URL.format(
            self.query,
            f"{arrow.utcnow().shift(days=-1).format('YYYY-MM-DDTHH:mm:ss')}Z",
            api_key)
        response = requests.get(url)
        if response.status_code == status.HTTP_200_OK:
            return response.json()
        else:
            # Trying the type system for the first time so this can be an issue.
            return dict()

    def get_or_create_yt_data(self, yt_data: dict) -> None:
        """
        We are not sure if the data is already in the db, therefore has to do
        this.
        :return:
        """
        video_list: list = yt_data.get('items')
        # This can be async.
        for video in video_list:
            # Won't be good to use get_or_create
            try:
                db_video_data = VideoData.objects.get(
                    video_id=video.get('id').get('videoId'))
                self.update_video(db_video_data, video)
            except ObjectDoesNotExist:
                self.create_video_data(video)
        pass

    def update_video(self, video_data: VideoData, video: dict):
        video_data.__dict__.update(self.create_db_dict(video))
        video_data.save()

    def create_video_data(self, video: dict) -> None:
        video_data_dict = self.create_db_dict(video)
        VideoData.objects.create(
            video_id=video_data_dict.get('video_id'),
            title=video_data_dict.get('title'),
            description=video_data_dict.get('description'),
            published_at=video_data_dict.get('published_at')
        )

    def create_db_dict(self, video: dict) -> dict:
        return {
            'video_id': video.get('id').get('videoId'),
            'title': video.get('snippet').get('title'),
            'description': video.get('snippet').get('description'),
            'published_at': arrow.get(video.get('snippet').get('publishedAt'))
        }
