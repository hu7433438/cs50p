import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if youtube := re.search(r"\"https?://(www\.)?youtube\.com/embed/(\w+)\"", s):
        return f"https://youtu.be/{youtube.group(2)}"


if __name__ == "__main__":
    main()
