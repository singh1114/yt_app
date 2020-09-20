from django.contrib import admin

from videos.models import VideoData


@admin.register(VideoData)
class VideoInfoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'title', 'description',
                    'published_at',)
    search_fields = ('video_id', 'title', 'description',)
