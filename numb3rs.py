import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.match(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$', ip):
        return True
    return False


if __name__ == "__main__":
    main()
