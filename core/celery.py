import os
from django.conf import settings

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.conf.enable_utc = False
app.conf.update(timezone=settings.CELERY_TIMEZONE)

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Config

app.conf.beat_schedule = {
    'create_monthly_sheet': {
        'task': 'reports.tasks.create_monthly_sheet',
        'schedule': crontab(0, 0, day_of_month='1')
    }
}
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
