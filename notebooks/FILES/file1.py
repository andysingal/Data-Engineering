from bs4 import BeautifulSoup
import requests

# Defining the url of the site
base_site = "https://en.wikipedia.org/wiki/Music"

# Making a get request
response = requests.get(base_site)
print(response.status_code)

# Extracting the HTML
html = response.content


soup = BeautifulSoup(html, "html.parser")

# with open('Wiki_response.html', 'wb') as file:
#     file.write(soup.prettify('utf-8'))

links = soup.find_all("a")
# print(len(links))

# for link in links:
#     print(link.get("href"))

table = soup.find('tbody')
# print(table)
# print(table.find_all("td"))
# isinstance(links,list)

# print(soup.find_all('a', class_ = 'mw-jump-link'))
a = soup.find('a', class_ = 'mw-jump-link')
# print(a.attrs)
# p = soup.find_all('p')[1]
# print(soup.text)
