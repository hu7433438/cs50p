import sys
import inflect
from datetime import date


def main():

    print(convert_date(input('Date of Birth: ')))


def convert_date(d):
    try:
        year, month, day = d.split("-")
        birthday = date(int(year), int(month), int(day))
        a = date.today() - birthday
        return f"{inflect.engine().number_to_words(a.days * 24 * 60, andword='')} minutes".capitalize()
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
