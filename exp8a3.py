# import required modules
from bs4 import BeautifulSoup
import requests

# get URL
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
page = requests.get("https://en.wikipedia.org/wiki/Main_Page", headers=headers)
# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
# create object
object = soup.find(id="mp-left")
# find tags
items = object.find_all(class_="mp-h2")
result = items[0]
# display tags
print(result.prettify())