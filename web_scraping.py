import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://blog.finxter.com/python-web-scraping-from-url-to-csv-in-no-time/#:~:text=Python%20CSV%20Module&text=It%20is%20simple%20and%20easy,first%2C%20import%20the%20csv%20module.&text=To%20write%20the%20scraped%20data,writerows()%20methods%20as%20required."

with open("scraped_data.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Data_Title", "Data_Content"])  # Header row

    for page_number in range(1, 6):  # Loop through page numbers 1 to 5
        url = base_url + str(page_number)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        