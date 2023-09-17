import logging
import json
# Get an instance of a logger
logger = logging.getLogger(__name__)
from core.utils import Property
from django.http import HttpResponse
# import web_scraping
from core.web_scraping import scrap
from mongoengine import Q

def my_cron_job():
    print('Hello World')
    logging.info("It's Working!")

# def my_cron_job_api(req):
#     user = User(email='aashish.gaba097@gmail.com', first_name='Aashish', last_name='Gaba')
#     user.save()
#     logging.info("It's Working!")
#     return HttpResponse("message")

def my_cron_job_api(req):
    city={"hyderabad": 269, "pune": 19}
    for key in city:
        list_data=scrap(key, city[key])
        # print(list_data)
        for i in range(0,len(list_data)):
            data=list_data[i]
            existing_properties = Property.objects(Q(link=data["link"]))
            if len(existing_properties) > 0:
                print("Property alread exists")
                continue
            print("Adding a new property...s")
            listing = Property(name=data["name"], cost=data["costs"], type=data["type"], area=data["area"], locality=data["locality"], link=data["link"], city=f"{key}")
            listing.save()
    
    return HttpResponse(json.dumps({
        "message": "data added",
        "listing": [list_data]
    }))
