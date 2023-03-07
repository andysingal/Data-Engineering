# Load the packages
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Defining the url of the site
base_site = "https://en.wikipedia.org/wiki/Music"

# Making a get request
response = requests.get(base_site)
print(response.status_code)

# Extracting the HTML
html = response.content

# Convert HTML to a BeautifulSoup object. This will allow us to parse out content from the HTML more easily.
# Using the default parser as it is included in Python
soup = BeautifulSoup(html, "html.parser")

# If we want all the results we use find_all()
links = soup.find_all('a')

link = links[26]

relative_url = link['href']
print(relative_url)
#Absolute url
full_url = urljoin(base_site,relative_url)
print(full_url)

#Extracting data from nested tags
clean_links = [l for l in links if  l.get('href') != None]
relative_urls = [l.get('href') for l in clean_links]
# print(relative_urls)

full_urls = [urljoin(base_site,url) for url in relative_urls]
# print(full_urls)

# internal_links = [url for url in full_urls if 'wikipedia.org' in url]
# print(internal_links)
clean_links = [l for l in links if  l.get('href') != None]
# print(clean_links)
# Getting all titles of links using a list comprehension
titles = [l.get('title') for l in clean_links]

# Removing the 'None' titles
clean_titles = [t for t in titles if t != None]
# print(clean_titles)
#h2
# Get the text
h2_strings = [h2.string for h2 in soup.find_all('h2')]
# print(h2_strings)
# #footer
# print(soup.find('div', id='footer'))

