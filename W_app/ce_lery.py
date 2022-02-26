import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Weather-App.settings')
app = Celery('Weather-App')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'Asia/Tashkent'

# app.conf.beat_schedule = {
#     'every_30_seconds': = {
#         'task': 'users.tasks.thirty_second_func',
# },
# }

