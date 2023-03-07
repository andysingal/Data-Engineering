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

# initialize list to store paragraph text for each webpage
par_text = []

# creating a loop counter
i = 0

# Loop through each URL in note_urls
for url in note_urls:

    # connect to every webpage
    note_resp = requests.get (url)

    # checking if the request is successful
    if note_resp.status_code == 200:  # Everything is OK!
        print ('URL #{0}: {1}'.format (i + 1,
                                       url))  # print out the number of iteration and the URL to keep track of place in loop

    else:  # Something is wrong!
        print ('Status code {0}: Skipping URL #{1}: {2}'.format (note_resp.status_code, i + 1, url))
        i = i + 1
        continue

    # get HTML from webpage
    note_html = note_resp.content

    # convert HTML to BeautifulSoup object
    note_soup = BeautifulSoup (note_html, 'lxml')

    # find all "p" tags on the webpage
    note_pars = note_soup.find_all ("p")

    # Get the text from each "p" tag
    text = [p.text for p in note_pars]

    # Append text from each "p" tag to our list, par_text
    par_text.append (text)

    # Incrementing the loop counter
    i = i + 1

page_text = ["".join(text) for text in par_text]

url_to_text = dict(zip(note_urls, page_text))
print(url_to_text['https://en.wikipedia.org/wiki/Music_theory'])


