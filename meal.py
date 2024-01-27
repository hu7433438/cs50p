#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/18 0:42
# @Author  : QingYang H.
# @File    : meal.py
def main():
    t = convert(input('What time is it? '))
    if 7 <= t <= 8:
        print('breakfast time')
    elif 12 <= t <= 13:
        print('lunch time')
    elif 18 <= t <= 19:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(':')
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
