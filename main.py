"""
Configuration for the main function.
"""
from crawler import Crawler
from collect import get_salary_value
from scraper import Soup


def main(salaries):
    """
    Function collects values from page,
    """
    values = []
    inst = Crawler()
    soup = Soup()
    for salary in salaries:
        values.append(get_salary_value(inst, soup, salary)[:-4])


if __name__ == "__main__":
    main()









if __name__ == '__main__':
    main(['1000', '2000'])