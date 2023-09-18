from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from core.cron import data_scrapping

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_scraping.settings')

app = Celery('scraping')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def hello_world(self):
    print('Hello world!')

@app.task(bind=True)
def run_scraping(self):
    print("Starting to run scheduled tasks")
    data_scrapping()
    print("Finished scrapping job.....")
