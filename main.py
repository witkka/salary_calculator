import time

from crawler.wynagrodzenia import Crawler
from scraper.soup import Soup
from retrying import retry
from crawler.retries import retry_if_page_crushed
from selenium.common.exceptions import TimeoutException
from crawler.constants import BASE_URL

@retry(stop_max_attempt_number=10, retry_on_exception=retry_if_page_crushed, wait_random_min=1000, wait_random_max=2000)
def main(gross_list):
    salaries= []
    w = Crawler()
    s = Soup()
    try:
        for salary in gross_list:
            w.navigate_to_website(BASE_URL)
            w.accept_cookies()
            w.enter_gross_value(salary)
        return salaries
    except TimeoutException:
        print("Time's out")











if __name__ == '__main__':
    main(['1000', '2000'])