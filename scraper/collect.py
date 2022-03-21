from crawler.wynagrodzenia import Wynagrodzenia
from retrying import retry
from crawler.retries import retry_is_page_crushed
from scraper.soup import Soup
import asyncio


"""helper function to collect single action async."""
@retry(retry_on_exception=retry_is_page_crushed, wait_random_min=1000, wait_random_max=2000)
def get_salary_value(salary):
    inst = Wynagrodzenia()
    inst.land_first_page()
    inst.accept_cookies()
    inst.type_in_salary(salary)
    soup = Soup().make_soup(inst.get_gross_salary())
    return Soup().get_salary(soup)


