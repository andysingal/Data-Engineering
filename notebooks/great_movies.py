from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/" \
      "https://www.empireonline.com/movies/features/best-movies-2/"
# Making a get request
response = requests.get(url)
print(response.status_code)
# print(response.text)
# Extracting the HTML
html = response.text
soup = BeautifulSoup(html, "html.parser")

#title
title = soup.select("h2")[0].getText()
print(title)

#movies
all_movies = soup.find_all(name="h3",class_="title")
movies_title = [movie.getText() for movie in all_movies]
movies = movies_title[::-1]

with open("movies.txt", 'w') as file:
    for movie in movies:
         file.write(f"{movie}\n")


