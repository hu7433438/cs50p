import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if t := re.search(r"^(1[0-2]|\d)(:[0-5]\d)? ([A|P]M) to (1[0-2]|\d)(:[0-5]\d)? ([A|P]M)$", s):
        hour_1, min_1, period_1, hour_2, min_2, period_2 = t.groups()
        hour_1, hour_2 = int(hour_1), int(hour_2)
        if period_1 == "AM" and hour_1 == 12:
            hour_1 = 0
        elif period_1 == "PM" and hour_1 != 12:
            hour_1 += 12
        if period_2 == "AM" and hour_2 == 12:
            hour_2 = 0
        elif period_2 == "PM" and hour_2 != 12:
            hour_2 += 12
        if min_1 is None:
            min_1 = ":00"
        if min_2 is None:
            min_2 = ":00"

        return f"{hour_1:02d}{min_1} to {hour_2:02d}{min_2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
