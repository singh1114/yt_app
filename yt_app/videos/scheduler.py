"""
It would be better if we use celery to run this operation.
Using basic all time running scheduler for now.
"""

import time

from videos.handlers.video_data import VideoDataFetchHandler


def video_scheduler():
    should_run = True
    while should_run:
        interval = 10
        should_run = VideoDataFetchHandler().fetch_and_insert_video_data()
        time.sleep(interval)
