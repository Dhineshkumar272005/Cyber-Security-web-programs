from bs4 import BeautifulSoup
import requests

# get URL
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
page = requests.get("https://en.wikipedia.org/wiki/Main_Page", headers=headers)
# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
# display scraped data
print(soup.prettify())