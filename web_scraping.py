import requests

url = "https://www.99acres.com/search/property/buy/hyderabad?city=269&preference=S&area_unit=1&res_com=R"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

try:
    response = requests.get(url, headers=headers)
    print(response)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

