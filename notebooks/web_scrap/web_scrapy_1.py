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

header = soup.find('head')
links = soup.find_all('a')

table = soup.find('body')

#Links -Absolute URL
link = links[26]
print(link.string)
print(link['href'])

relative_url = link['href']
full_url = urljoin(base_site,relative_url)

clean_links = [l for l in links if l.get('href') != None]
relative_urls = [l.get('href') for l in clean_links]

full_urls = [urljoin(base_site, url) for url in relative_urls]

internal_links = [url for url in full_urls if 'wikipedia.org' in url]
print()

