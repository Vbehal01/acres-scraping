import requests
from bs4 import BeautifulSoup as BS



def scrap(city_key, city_code):
    url = f"https://www.99acres.com/search/property/buy/{city_key}?city={city_code}&preference=S&area_unit=1&res_com=R"
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers)
        # if response.status_code == 200:
        #     # html_content = response.text
        # else:
        #     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        #     exit()

        d1=open("core/abc3.txt","r")
        html_content=d1.read()
        soup=BS(html_content, 'html.parser')
        section_divs = soup.find("div", attrs={"class":"pageComponent undefined"})
        data=section_divs.find_all("section", attrs={"data-hydration-on-demand": "true"})
        final_listing=[]
        for div in data:
            name=div.find("a", attrs={"class": "projectTuple__projectName projectTuple__pdWrap20 ellipsis"})
            name2=div.find("a", attrs={"class": "srpTuple__dFlex"})
            name3=div.find("td", attrs={"id ": "srp_tuple_society_heading"})
            exact_name=""
            if(name):
                exact_name = name.text.strip()
                # print("name: ",name.text.strip())
            elif(name2):
                exact_name = name2.text.strip()
                # print("name: ",name2.text.strip())
            else:
                exact_name = name3.text.strip()
                # print("name: ",name3.text.strip())

            cost=div.find("td" , attrs={"id":"srp_tuple_price"})
            costs=div.find("span" , attrs={"class":"list_header_bold configurationCards__srpPriceHeading configurationCards__configurationCardsHeading"})
            cost_unit=div.find("span", attrs={"id": "srp_tuple_price_unit"})
            if(cost):
                # property_cost = None
                # print("cost", cost)
                # print("cost text", cost.text)
                # print("cost contents", cost.contents)
                exact_cost=""
                property_cost = cost.text
                if len(cost.contents) > 1:
                    if(cost_unit):
                        property_cost=(cost.contents[0].strip())+ (cost_unit.text.strip())
                        exact_cost=property_cost.strip()
                        # print("cost: ",property_cost.strip())
                    else:
                        property_cost=cost.contents[0].strip()
                        exact_cost=property_cost.strip()
                        # print("cost: ",property_cost.strip())
            else:
                # costs=costs.text.strip()
                exact_cost=costs.text.lstrip()
                # print("costs:",costs.text.lstrip())

            type=div.find("h2")
            type=type.text.split("in")
            exact_type=""
            exact_type=type[0].strip()
            # print("type: ",type[0].strip())

            area=div.find("td", attrs={"id":"srp_tuple_primary_area"})
            area_unit=div.find("span", attrs={"id":"srp_tuple_primary_area_unit"})
            area2=div.find_all("div", attrs={"class":"configurationCards__cardAreaHeading ellipsis"})
            exact_area=""
            if(area):
                exact_area=(area.contents[0].strip())+(area.contents[1].text.strip())
                # print("area: ",(area.contents[0].strip())+(area.contents[1].text.strip()))
            else:
                for i in area2:
                    i=i.find("span", attrs={"class":"caption_subdued_medium configurationCards__cardAreaSubHeadingOne"})
                    exact_area=i.text.strip()
                    # print("area2: ",i.text.strip())
                
            locality=type[1].split(", ")
            exact_locality=""
            exact_locality=locality[0].strip()
            # print("locality: ", locality[0].strip())

            link=div.find("a", attrs={"class": "body_med srpTuple__propertyName"})
            link2=div.find("a", attrs={"class": "projectTuple__projectName projectTuple__pdWrap20 ellipsis"})
            exact_link=""
            if(link):
                exact_link=link.get('href').strip()
                # print("link: ",link.get('href').strip())
            else:
                exact_link=link2.get('href').strip()
                # print("link2: ",link2.get('href').strip())
            # print()
            final_listing.append({
                "name": exact_name,
                "costs": exact_cost,
                "type": exact_type,
                "area": exact_area,
                "locality": exact_locality,
                "link": exact_link
                })
            # print(final_listing)
        
        return final_listing

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")   
