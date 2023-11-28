"""
Libraries required: 
pip install requests
pip install bs4
"""
import pprint
import requests
from bs4 import BeautifulSoup

# url = "https://foodmandu.com/"
# r = requests.get(url)


# soup = BeautifulSoup(source_code)

# menu_url = soup.findAll("div", {
# 	"class": "listing"})

# for listing in listing_div:
# 	print(listing.text.strip())



# url = "https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId=1027&show=/"
# r= requests.get(url)
# all_menus = r.json()
# print (r.text)

# for menu in all_menus:
#     print("name: ", menu ['name'], menu['price'])


class FoodmanduScraper:
    def __init__(self):
        self.url = "https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId=(restaurant_id)&show=/"

    def scrape_menu(self, restaurant_id):
        r = requests.get(self.url)
        all_menus = r.json()
        all_menus = all_menus [0] ['items']
        for menu in all_menus:
            print("name: ", menu['name'], menu['price'])
            tmp= {
                "name": menu['name'],
                "price": menu['price']
            }
            output.append{tmp}

        headers = output [0].keys()

        with open('foodmandu-menus.csv', 'w') as file_object:
            dict_writer = csv.Dictwriter(file_object, headers)
            dict_writer.writeheader ()
            dict_writer.writerows(output)
        return all_menus

s = FoodmanduScraper()
s.scrape_menu(1027)
