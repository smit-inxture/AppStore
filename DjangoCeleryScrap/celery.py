from celery import Celery
import os

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoCeleryScrap.settings')

app = Celery('DjangoCeleryScrap')

app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()
# app.conf.timezone   = 'Asia/Kolkata'

#Here We Can Also Schedule Task For Particular Time Also After server Minutes
app.conf.beat_schedule = {
    'change-financial-year-dates': {
        'task': 'play_store.tasks.app_details_task',
        'schedule': crontab(hour='17', minute='57'),
    }
}