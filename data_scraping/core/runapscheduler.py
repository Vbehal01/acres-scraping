# import logging

# from django.conf import settings

# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.triggers.cron import CronTrigger
# from django.core.management.base import BaseCommand
# from django_apscheduler.jobstores import DjangoJobStore
# from django_apscheduler.models import DjangoJobExecution
# from django_apscheduler import util
# from core.cron import data_scrapping

# logger = logging.getLogger(__name__)


# def my_job():
#   data_scrapped=data_scrapping(req)
#   return data_scrapped


# @util.close_old_connections
# def delete_old_job_executions(max_age=604_800):
#   DjangoJobExecution.objects.delete_old_job_executions(max_age)


# class Command(BaseCommand):
#   help = "Runs APScheduler."

#   def handle(self, *args, **options):
#     scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
#     scheduler.add_jobstore(DjangoJobStore(), "default")

#     scheduler.add_job(
#       my_job,
#       trigger=CronTrigger(hour="8,20", minute="0"),  # Every 10 seconds
#       id="my_job",  # The `id` assigned to each job MUST be unique
#       max_instances=1,
#       replace_existing=True,
#     )
#     logger.info("Added job 'my_job'.")

#     scheduler.add_job(
#       delete_old_job_executions,
#       trigger=CronTrigger(
#         day_of_week="mon", hour="00", minute="00"
#       ), 
#       id="delete_old_job_executions",
#       max_instances=1,
#       replace_existing=True,
#     )
#     logger.info(
#       "Added weekly job: 'delete_old_job_executions'."
#     )

#     try:
#       logger.info("Starting scheduler...")
#       scheduler.start()
#     except KeyboardInterrupt:
#       logger.info("Stopping scheduler...")
#       scheduler.shutdown()
#       logger.info("Scheduler shut down successfully!")

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .cron import data_scrapping

def start():
  scheduler=BackgroundScheduler()
  scheduler.add_job(data_scrapping, 'interval', hours=12)
  scheduler.start()