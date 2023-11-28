import requests
from bs4 import BeautifulSoup
url="https://foodmandu.com/Restaurant/Details/269"
r=requests.get(url)
source_code = r.text

soup = BeautifulSoup(source_code)
listing_div = soup.findAll ("div",{
    "class":"menu__content wrap"
})
for listing in listing_div:
    print(listing.text.strip())