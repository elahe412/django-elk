# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'log_test.settings')

# create a Celery instance
app = Celery('log_test')

# load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto-discover tasks in all installed apps
app.autodiscover_tasks()
