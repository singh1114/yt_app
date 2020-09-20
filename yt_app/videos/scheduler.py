"""
It would be better if we use celery to run this operation.
Using basic all time running scheduler for now.
"""
from videos.handlers.video_data import VideoDataFetchHandler
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        VideoDataFetchHandler().fetch_and_insert_video_data,
        'interval', seconds=10)
    scheduler.start()
