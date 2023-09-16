from mongoengine import *
connect()

class property(Document):
    Name = StringField(required=True)
    Cost = StringField(max_length=50)
    Type = StringField(max_length=50)
    Area = StringField(max_length=50)
    Locality = StringField(max_length=50)
    City = StringField(max_length=50)
