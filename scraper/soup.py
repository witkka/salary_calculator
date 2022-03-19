from bs4 import BeautifulSoup, SoupStrainer

class Soup:
    def __init__(self):
        pass

    def strain_soup(self):
        return SoupStrainer('div', attrs={'class': 'fullbox count-salary mbot20'})

    def make_soup(self, page_source):
        strainer = self.strain_soup()
        return BeautifulSoup(page_source, 'html.parser', parse_only=strainer)

    def get_salary(self, soup):
        return soup.get_text()

