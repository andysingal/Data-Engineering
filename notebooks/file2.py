from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"
# Making a get request
response = requests.get(url)
print(response.status_code)
# print(response.text)
# Extracting the HTML
html = response.text
soup = BeautifulSoup(html, "html.parser")

# articles = soup.select(".titleline > a")
articles = soup.findAll(name="span", class_="titleline")
article_texts = []
article_links = []
for article in articles:
    article_texts.append (article.getText ())
    article_links.append (article.contents[0].get ("href"))


article_upvotes = [int(score.getText().strip(" points"))  for score in  soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
# print(article_texts[largest_number])
# print(article_links[largest_number])



