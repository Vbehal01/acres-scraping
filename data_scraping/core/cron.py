import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
from core.utils import User
from django.http import HttpResponse

def my_cron_job():
    print('Hello World')
    logging.info("It's Working!")

def my_cron_job_api(req):
    user = User(email='aashish.gaba097@gmail.com', first_name='Aashish', last_name='Gaba')
    user.save()
    logging.info("It's Working!")
    return HttpResponse("message")