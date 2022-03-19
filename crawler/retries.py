from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, NoSuchWindowException, WebDriverException

def retry_is_page_crushed(exception):
    return isinstance(exception, WebDriverException)

def retry_if_window_not_found(exception):
    return isinstance(exception, NoSuchWindowException)

def retry_if_element_not_found(exception):
    return isinstance(exception, NoSuchElementException)

