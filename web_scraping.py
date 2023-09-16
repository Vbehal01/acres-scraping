import requests
# from bs4 import BeautifulSoup
 
 
# Making a GET request
r1 = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print("r1: ",r1)
r = requests.get('https://www.99acres.com/search/property/buy/hyderabad?city=269&preference=S&area_unit=1&res_com=R')
 
# check status code for response received
# success code - 200

print(r)