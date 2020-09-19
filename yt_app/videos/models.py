from django.db import models

from base.models import AbstractBaseModel


class VideoData(AbstractBaseModel):
    video_id = models.CharField(
        max_length=1000, blank=True, null=True, db_index=True)
    title = models.CharField(max_length=2000, db_index=True, null=True)
    description = models.CharField(max_length=5000, db_index=True, null=True)
    # TODO check later if this can be date field.
    published_at = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.video_id}"

    class Meta:
        ordering = ('-published_at',)
