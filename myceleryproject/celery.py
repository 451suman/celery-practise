from datetime import timedelta
import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myceleryproject.settings")

app = Celery("myceleryproject")
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
app.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://redis:6379/0"
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f"Request: {self.request!r}")

# celery beat
# normal

# app.conf.beat_schedule = {
#     "every-10-seconds": {
#         "task": "myapp.tasks.clear_session_cache",
#         "schedule": 10,
#         "args": ("123",),
#     }
# }

# using time delta

# app.conf.beat_schedule = {
#     "every-10-seconds": {
#         "task": "myapp.tasks.clear_session_cache",
#         "schedule": timedelta(seconds=10),
#         "args": ("123",),
#     }
# }

# useing Corntabs


app.conf.beat_schedule = {
    "every-1-min": {
        "task": "myapp.tasks.clear_session_cache",
        "schedule": crontab(minute="*/1"),
        "args": ("123",),
    }
}
