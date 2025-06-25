import requests
from bs4 import BeautifulSoup as BS
from core.constants import FILE_PATH, UNSCRAPPED_DATA

def read_file_content(filepath: str):
    file_content=""
    with open(filepath,"r") as f:
        file_content=f.read()
    return file_content

def extract_all_listings_elements(page_html):
    section_divs = page_html.find("div", attrs={"class": "pageComponent undefined"})
    section_listing_elements = section_divs.find_all("section", attrs={"data-hydration-on-demand": "true"})
    return section_listing_elements

def extract_name(listing_element):
    name1 = listing_element.find("a", attrs={"class": "projectTuple__projectName projectTuple__pdWrap20 ellipsis"})
    name2 = listing_element.find("a", attrs={"class": "srpTuple__dFlex"})
    name3 = listing_element.find("td", attrs={"id ": "srp_tuple_society_heading"})
    name = name1 if name1 else (name2 if name2 else name3)
    if name:
        return name.text.strip()
    else:
        return name

def extract_cost(listing_element):
    cost=listing_element.find("td" , attrs={"id":"srp_tuple_price"})
    costs=listing_element.find("span" , attrs={"class":"list_header_bold configurationCards__srpPriceHeading configurationCards__configurationCardsHeading"})
    cost_unit=listing_element.find("span", attrs={"id": "srp_tuple_price_unit"})
    extract_cost=""
    if(cost):
        if len(cost.contents) > 1:
            if(cost_unit):
                property_cost=(cost.contents[0].strip())+ (cost_unit.text.strip())
                exact_cost=property_cost.strip()
            else:
                property_cost=cost.contents[0].strip()
                exact_cost=property_cost.strip()
    else:
        exact_cost=costs.text.lstrip()
        return exact_cost

def extract_type(listing_element):
    listing_type=listing_element.find("h2")
    listing_type=listing_type.text.split("in")
    return listing_type[0].strip()

def extract_locality(listing_element):
    listing_locality=listing_element.find("h2")
    listing_locality=listing_locality.text.split("in")
    listing_locality=listing_locality[1].split(",")
    return listing_locality[0].strip()


def extract_area(listing_element):
    area=listing_element.find("td", attrs={"id":"srp_tuple_primary_area"})
    area_unit=listing_element.find("span", attrs={"id":"srp_tuple_primary_area_unit"})
    area2=listing_element.find_all("div", attrs={"class":"configurationCards__cardAreaHeading ellipsis"})
    exact_area=""
    if(area):
        exact_area=(area.contents[0].strip())+(area.contents[1].text.strip())
    else:
        for i in area2:
            i=i.find("span", attrs={"class":"caption_subdued_medium configurationCards__cardAreaSubHeadingOne"})
            exact_area=i.text.strip()
    return exact_area

def extract_link(listing_element):
    link=listing_element.find("a", attrs={"class": "body_med srpTuple__propertyName"})
    link2=listing_element.find("a", attrs={"class": "projectTuple__projectName projectTuple__pdWrap20 ellipsis"})
    exact_link=link if link else link2
    return exact_link.get('href').strip()

def scrap(city_key, city_code):
    scraped_listing=[]
    try:
        if(UNSCRAPPED_DATA==True):
            page_html=read_file_content(FILE_PATH)
        else:
            url = f"https://www.99acres.com/search/property/buy/{city_key}?city={city_code}&preference=S&area_unit=1&res_com=R"
            headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
            response = requests.get(url, headers=headers)
            page_html = response.text

        page_html=BS(page_html, 'html.parser')
        listing_elements=extract_all_listings_elements(page_html)
        for listing_element in listing_elements:
            property_name=extract_name(listing_element)
            property_cost=extract_cost(listing_element)
            property_type=extract_type(listing_element)
            property_locality=extract_locality(listing_element)
            property_area=extract_area(listing_element)
            property_link=extract_link(listing_element)

            scraped_listing.append({
                "name": property_name,
                "costs": property_cost,
                "type": property_type,
                "area": property_area,
                "locality": property_locality,
                "link": property_link
                })
        
        return scraped_listing

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")   
