import logging
import json
logger = logging.getLogger(__name__)
from core.utils import Property, Record
from django.http import HttpResponse
from core.web_scraping import scrap
from mongoengine import Q

def data_scrapping():
    city={"pune": 19, "delhi": 1075722, "mumbai-all": 12, "lucknow": 205, "agra": 197, "ahmedabad-all": 45, "kolkata-all": 25, "jaipur": 177, "chennai-all": 32, "bangalore-all": 20}
    count=0
    data_count=0
    data_exist_count=0
    for key in city:
        list_data=scrap(key, city[key])
        data_count=data_count+len(list_data)
        for i in range(0,len(list_data)):
            data=list_data[i]
            existing_properties = Property.objects(Q(link=data["link"]))
            if len(existing_properties) > 0:
                logger.info("Property alread exists")
                data_exist_count=data_exist_count+len(existing_properties)
                continue
            else:
                logger.info("Adding a new property...s")
                listing = Property(name=data["name"], cost=data["costs"], type=data["type"], area=data["area"], locality=data["locality"], link=data["link"], city=f"{key}")
                listing.save()
                count=count+1

    record=Record(total_data_scrapped=data_count, already_inserted_data=data_exist_count, new_inserted_data=count)
    record.save()
    return HttpResponse(json.dumps({
        "listing": [list_data],
        "record": {
            "total_scraped": data_count,
            "new_listings": count,
            "existing": data_exist_count
        }
    }))
