# Load the packages
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Defining the url of the site
base_site = "https://en.wikipedia.org/wiki/Music"
# Extracting the HTML
# Making a get request
response = requests.get(base_site)
print(response.status_code)

# Extracting the HTML
html = response.content
soup = BeautifulSoup(html, "html.parser")

div_notes = soup.find_all("div",{"role": "note"})
print(div_notes[0].find('a'))

div_links = []
for div in div_notes:
    anchors = div.find_all('a')
    div_links.extend(anchors)



note_urls = [urljoin(base_site, l.get('href')) for l in div_links]
print(note_urls, end="")

