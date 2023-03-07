import requests
import time

from pages.all_books_page import AllBooksPage

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books
# for book in books:
#     print(book)
_books = []

start = time.time()
for page_num in range(page.page_count):
    page_start = time.time()
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    _books.extend(page.books)
print(f'Total took {time.time() - start}')

books = _books
