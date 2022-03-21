"""
Configuration necessary for the 'det_salary_value_function'.
retry is a module enabling a number of retries after function returns false
"""
from retrying import retry
from retries import retry_if_did_not_produce_data


@retry(stop_max_attempt_number=10, retry_on_result=retry_if_did_not_produce_data)
def get_salary_value(inst, soup, salary):
    """Function consolidating all steps to obtain data from page"""
    if inst.land_first_page():
        print("landed first page")
        if inst.accept_cookies():
            print("accepted cookies")
            if inst.type_in_salary(salary):
                print("typed in salary")
                page = inst.get_page_html()
                if page is not None:
                    salary = soup.get_salary(soup.make_soup(page))
                    if salary is not None or len(salary) != 0:
                        inst.close_connection()
                        return salary
                    else:
                        print("couldn't collect data")
                        inst.close_connection()
                        return False
            else:
                print("couldn't type in salary")
                return False
        else:
            print("couldn't accept cookies")
            return False
    else:
        print("didn't land first page")
        return False
