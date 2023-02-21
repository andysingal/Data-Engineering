from bs4 import BeautifulSoup
import lxml
with open('website.html') as file:
    content = file.read()

soup = BeautifulSoup(content,"html.parser")
# print(soup.prettify())
# print(soup.title.string)
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find_all(class_="heading")
print(heading)
# print(heading.getText())

section_heading = soup.find_all(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)
