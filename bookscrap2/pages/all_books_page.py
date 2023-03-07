from locators.all_books_page import AllBooksPageLocators
from parsers.book import BookParser
from bs4 import BeautifulSoup

class AllBooksPage:
        def __init__(self, page):
            self.soup = BeautifulSoup (page, 'html.parser')

        @property
        def books(self):

            return [BookParser(e) for e in self.soup.select (AllBooksPageLocators.BOOKS)]




