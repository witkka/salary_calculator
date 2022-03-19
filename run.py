from calculator.collect import get_salary_value

import asyncio


def main(data):
    for d in data:
        print(d)
        print(get_salary_value(d))


if __name__ == '__main__':
    main(['1000', '2000', '3000'])