from bs4 import BeautifulSoup
import requests,pprint
import pandas as pd
import lxml
import smtplib, ssl,os
import certifi

# Defining the url of the site
HEADERS = {
    "User-Agent": "Defined",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4",
}
LINK = "https://www.amazon.com/Instant-Pot-Electric-Sterilizer-Stainless/dp/" \
       "B09MZTSSR2/ref=sr_1_1_sspa?crid=2A89WN0S6I2NE&keywords=Instant%2BPot%2BDuo%2BEvo&qid=1677574180&" \
       "sprefix=instant%2Bpot%2Bduo%2Bevo%2Caps%2C689&sr=8-1-spons&spLa=" \
       "ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUVVLTlZYWUtMQVhVJmVuY3J5cHRlZElkPUEwNTA2MjA3Mks5MkdCVTI0NTZVQyZlbmNyeXB0ZWRBZElkPUEwNDY4MDM2M" \
       "zVETzAwWTZGUDJRJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"

response = requests.get (LINK, headers=HEADERS)
website = response.content

soup = BeautifulSoup (website, "lxml")

price_tag = soup.find(name='span', class_= 'a-offscreen')
price = float(price_tag.get_text().split("$")[1].strip())
# print(price)

title = soup.find(id="productTitle").get_text().strip()
# print(title)

if price < 150:
    message = f"{title} is now ${price}"
    context = ssl.create_default_context (cafile=certifi.where())
    receiver = "andysingal@gmail.com"
    port = 587
    username = "andysingal@gmail.com"
    password = os.getenv ("PASSWORD")
    with smtplib.SMTP ("smtp.gmail.com", port) as connection:

        connection.starttls()
        result = connection.login (username, password)
        connection.sendmail(
            from_addr=username,
            to_addrs=receiver,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{LINK}".encode("utf-8")
        )






