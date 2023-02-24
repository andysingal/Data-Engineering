import requests
from send_email import send_email

api_key = "11efec15d52440909807050a52f75c7a"
topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-01-23&" \
      "sortBy=publishedAt&" \
      "apiKey=11efec15d52440909807050a52f75c7a&" \
      "language=en"
request = requests.get(url)
# print(request.status_code)


# get a dictionary with data
content = request.json()

body = ""

for article in content["articles"][:20]:
      if article["title"] is not None:
          body = "Subject: Today's news" + "\n" + body + article["title"] + "\n"\
                 + article["description"]\
                 + "\n"+ article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

