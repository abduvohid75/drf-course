from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

celery = Celery(__name__)
celery.config_from_object(__name__)
app = Celery('main')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-notification-every-minute': {
        'task': 'habits.tasks.send_notification',
        'schedule': 60.0,
    },
}
