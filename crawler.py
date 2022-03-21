"""
Configuration for the crawler class
Selenium is a module that enables crawling and scraping dynamic pages.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.service import Service
import time
import os
from selenium.webdriver.common.keys import Keys
from CONSTANTS import BASE_URL

dir_path = os.path.dirname(__file__)
file_name = "/chromedriver.exe"
file_path = dir_path + file_name


class Crawler:
    """Method responsible for initializing crawler class."""

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver_path = file_path
        os.environ["PATH"] += driver_path
        self.driver = webdriver.Chrome(service=Service(driver_path), options=options)
        self.driver.wait = WebDriverWait(self.driver, 10)

    def land_first_page(self):
        """Method responsible for landing firs page, returns True, if page could be accessed
        if page could not be accessed, returns False"""
        try:
            self.driver.get(BASE_URL)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def accept_cookies(self):
        """Method responsible for accepting cookies
        It sleeps for 5 seconds allowing page to fully load
        It switches driver to iframe, finds and clicks 'accept all' button
        If the iframe or buttons couldn't be found, returns False"""
        time.sleep(5)
        self.driver.switch_to.frame("cmp-iframe")
        try:
            element = self.driver.find_elements(By.XPATH, "//button")
            element[1].click()
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def type_in_salary(self, keyword):
        """Method responsible for typing in dalary values.
        If values could be typed in, it returns True
        if it could not find element it returns False"""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "sedlak_calculator_earnings"))
            )
            element.clear()
            element.send_keys(keyword)
            element.send_keys(Keys.RETURN)
            return True
        except (NoSuchElementException, WebDriverException, TimeoutException):
            return False

    def get_page_html(self):
        """Method responsible for collecting page html.
        It returns True, if it collected data,
        if not, returns False"""
        try:
            html = self.driver.page_source
            return html
        except (WebDriverException, TimeoutException):
            return False

    def close_connection(self):
        """Method responsible for closing connection"""
        self.driver.quit()
