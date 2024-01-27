<<<<<<< HEAD
s = input('Input: ')
for c in s:
    if c.lower() not in 'aeiou':
        print(c, end="")
=======
#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/21 19:29
# @Author  : QingYang H.
# @File    : twttr.py


def main():
    print(shorten(input('Input: ')))


def shorten(word):
    short_str = ''
    for c in word:
        if c not in 'aeiou':
            short_str += c
    return short_str


if __name__ == "__main__":
    main()
>>>>>>> cs50/problems/2022/python/tests/twttr
