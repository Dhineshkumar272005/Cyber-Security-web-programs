# import required modules
from bs4 import BeautifulSoup
import requests

# get URL
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
page = requests.get("https://en.wikipedia.org/wiki/Main_Page", headers=headers)
# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
list(soup.children)

# find all occurrence of p in HTML
# includes HTML tags
print(soup.find_all('p'))
print('\n\n')

# return only text
# does not include HTML tags
print(soup.find_all('p')[0].get_text())