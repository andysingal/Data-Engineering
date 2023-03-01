import pandas
import requests
from bs4 import BeautifulSoup
# Getting the webpage
link = "http://webscraperio.us-east-1.elasticbeanstalk.com/test-sites/e-commerce/static/computers/tablets?page="

# List of all the products on the website
products = []

for page in range (1, 5):
    # Concatenating the link with each page number
    webpage = requests.get (link + str (page))

    # Loading the content
    content = webpage.content

    # Parsing the content
    result = BeautifulSoup (content, 'html.parser')

    # Identifying the products on the page by the div tag and the class name
    products_on_page = result.find_all ("div", {"class": "col-sm-4 col-lg-4 col-md-4"})

    # Appending each product on each page to the list of products
    for product in products_on_page:
        products.append (product)

# print(len(products))

# Creating a list for each of the desired piece of information
names = []
links = []
prices = []

# Iterating over the list of products and extracting the necessary info
for item in products:
    names.append (item.a.string)
    links.append ("https://www.webscraper.io" + item.a['href'])
    prices.append (item.h4.string)

# print(names, len(names))
# print(links, len(links))
# print(prices, len(prices))

data = list (zip (names, links, prices))

# Creating the Pandas dataframe
d = pandas.DataFrame (data, columns=['Name', 'Link', 'Price'])

# Writing the dataframe to a new Excel file
try:
    d.to_excel ("Products.xlsx")

except:
    print ("\nSomething went wrong! Please check your code.")

else:
    print ("\nWeb data successfully written to Excel.")

finally:
    print ("\nQuitting the program. Bye!")