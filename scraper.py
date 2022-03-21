"""
Configuration of the Soup class.
bs4 is a library responsible for scraping data from pages.
"""
from bs4 import BeautifulSoup, SoupStrainer


class Soup:
    def __init__(self):
        pass


    def strain_soup(self):
        """Method responsible for straining - limiting data for further processing"""
        return SoupStrainer("div", attrs={"class": "fullbox count-salary mbot20"})

    def make_soup(self, page_source):
        """Method responsible for creating soup object"""
        strainer = self.strain_soup()
        return BeautifulSoup(page_source, "html.parser", parse_only=strainer)


    def get_salary(self, soup):
        """Method responsible for extracting string from <span>"""
        return soup.span.string
