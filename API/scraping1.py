from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"
response = requests.get(url)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

articles  = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText ()
    link = article_tag.find(name="a").get("href")
    article_texts.append(text)
    article_links.append (link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print (article_texts)
print (article_links)
print (article_upvotes)