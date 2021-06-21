from bs4 import BeautifulSoup
import requests
from csv import writer


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
}

url = "https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi"

string_list = list(url)
string_list[50] = "4"
new_url = "".join(string_list)



page = requests.get(new_url,headers=header)

soup = BeautifulSoup(page.content,'html.parser')

lists = soup.find_all('div',class_ = "filter-property-list")


with open('housing.csv','w',encoding='utf-8',newline='') as f:

    thewriter = writer(f)
    header = ['Name','Price','Price_Per_Unit','Area','Facing','Status','Owner','Amenities']
    thewriter.writerow(header)

    for list in lists:
        size = list.find('h1', class_ = 'filter-pro-heading').text[:5]
        price = list.find('span' , class_ = "price").text
        price_per_unit = list.find('span' , class_ = "price-per-unit").text
        name = list.find('span').text[2:]
        area = list.find('div',class_ = "col-4").text[4:]
        facing = list.find_all('div',class_ = "col-3")[1].text[6:]
        status = list.find('div',class_ = "col-5").text[6:]
        owner = list.find('span' , class_ = "owner-name").text

        amenities = list.find('ul',class_ = "pro-list").text.replace('\n','-')

        info = [name,price,price_per_unit,area,facing,status,owner,amenities]

        thewriter.writerow(info)
    



