from mongoengine import *
connect()

class Property(Document):
    name = StringField(max_length=500)
    cost = StringField(max_length=500)
    type = StringField(max_length=50)
    area = StringField(max_length=50)
    locality = StringField(max_length=50)
    city = StringField(max_length=50)
    link=StringField(max_length=200)

class Record(Document):
    total_data_scrapped= IntField()
    already_inserted_data= IntField()
    new_inserted_data= IntField()
