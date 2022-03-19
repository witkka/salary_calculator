import os
from selenium import webdriver
from crawler.constants import BASE_URL
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException, NoSuchWindowException, WebDriverException
import time
from retrying import retry
from crawler.retries import retry_if_window_not_found, retry_if_element_not_found


class Wynagrodzenia(webdriver.Chrome):
    def __init__(self, driver_path=r"\chromedriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Wynagrodzenia, self).__init__()
        self.implicitly_wait(30)
        self.maximize_window()

    def land_first_page(self):
        self.get(BASE_URL)
        print('wchodzę na stronę')

    def accept_cookies(self):
        time.sleep(5)
        #print('start looking')
        self.switch_to.frame('cmp-iframe')
        #print('found frame')
        try:
            element = self.find_elements(By.XPATH, '//button')
            #print('znaleziony')
            print('akceptuje cookies')
            return element[1].click()
        except NoSuchElementException:
            print('nie ma')
            return False

    @retry(retry_on_exception=retry_if_element_not_found, wait_random_min=1000, wait_random_max=2000)
    @retry(retry_on_exception=retry_if_window_not_found, wait_random_min=1000, wait_random_max=2000)
    def type_in_salary(self, keyword):
        print('szukam elementu "salary"')
        element = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.ID, 'sedlak_calculator_earnings')))
        print('znaleziony elemenet "salary"')
        element.clear()
        print('element wyczyszczony')
        element.send_keys(keyword)
        print('dane wpisane')
        element.send_keys(Keys.RETURN)

    @retry(retry_on_exception=retry_if_element_not_found, wait_random_min=1000, wait_random_max=2000)
    @retry(retry_on_exception=retry_if_window_not_found, wait_random_min=1000, wait_random_max=2000)
    def get_gross_salary(self):
        print('szukam wyników')
        #element = WebDriverWait(self, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#main-container > div.fullbox.count-salary.mbot20')))
        #print(element.text)
        return self.page_source

    def change_criteria(self):
        print('zmieniam kryteria')
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a*[@id="main-container"]/div[3]/div/div/div[4]/a'))).click()

