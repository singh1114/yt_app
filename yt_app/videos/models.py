from django.db import models

from base.models import AbstractBaseModel


class VideoData(AbstractBaseModel):
    video_id = models.CharField(
        max_length=50, blank=True, null=True, unique=True)
    # TODO optimize the max_length by researching about total title size
    title = models.CharField(max_length=2000, null=True)
    # TODO optimize the max_length by researching about total description size
    description = models.CharField(max_length=5000, null=True)
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.video_id}"

    class Meta:
        ordering = ('-published_at',)
