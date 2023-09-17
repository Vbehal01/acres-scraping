import requests
from bs4 import BeautifulSoup as BS

url = "https://www.99acres.com/search/property/buy/hyderabad?city=269&preference=S&area_unit=1&res_com=R"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

try:
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        html_content = response.text
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        exit()

    # soup=BS(html_content, 'html.parser')
    # section_divs = soup.find_all("div", attrs={"class":"pageComponent undefined"})
    # print(section_divs)
    # for div in section_divs:
    #     data=div.find_all("class", attrs={"data-hydration-on-demand": "true"})
    #     for i in data :
    #         print(i)
    #         print(i.find_all("h2", class_="srpTuple__tupleTitleOverflow"))
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
