import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

def my_cron_job():
    print('Hello World')
    logging.info("It's Working!")

def my_cron_job_api(req):
    print(req)
    print('Hello World')
    logging.info("It's Working!")
    return {
        "abc": "message"
    }