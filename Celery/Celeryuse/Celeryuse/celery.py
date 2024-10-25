import os

from django.conf import settings

from celery import Celery
from time import sleep

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celeryuse.settings')

app = Celery('Celeryuse')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# @app.task
# def add(x,y):
#     sleep(60)
#     return x+y

app.conf.broker_connection_retry_on_startup = True
##Method 2 Celery beat schedule task
app.conf.beat_schedule = {
    'Every_10_sec':{
        'task':'Scheduled Task',
        'schedule':10,
        'args':('1111',)
    }
}