from bs4 import BeautifulSoup
import requests

# Defining the url of the site
base_site = "https://www.billboard.com/charts/hot-100/2000-08-12"

# Making a get request
response = requests.get(base_site)
print(response.status_code)

# Extracting the HTML
html = response.content
soup = BeautifulSoup(html, "html.parser")

songs = soup.find_all(name= "h2",class_='c-title')
title = songs.getText()
print(title)

