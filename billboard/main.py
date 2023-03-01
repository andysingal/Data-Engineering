from bs4 import BeautifulSoup
import requests,pprint
import pandas as pd

# Defining the url of the site
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
base_site = f"https://www.billboard.com/charts/hot-100/{date}"

# Making a get request
response = requests.get(base_site)
print(response.status_code)

# Extracting the HTML
html = response.content
soup = BeautifulSoup(html, "html.parser")
title = soup.find('h2', class_='lrv-u-padding-r-00@mobile-max')
print(title.getText(strip=True))

song_titles = soup.select('.lrv-u-width-100p #title-of-a-story')
songs_and_footers = [song.getText(strip="\n\t") for song in song_titles]
songs = songs_and_footers[1:len(song_titles)-4]
print(len(songs))

#Artists name
artist_name = soup.select('.o-chart-results-list__item.lrv-u-flex-grow-1 >span.c-label:nth-child(2)')
artist = [artist.getText(strip=True) for artist in artist_name]
print(len(artist))

#TABLE_VISUALIZATION
my_dict = {'Top_Songs': songs,'Artists': artist}

df = pd.DataFrame.from_dict(my_dict, orient='index')
df = df.transpose()
pprint.pprint(df)
