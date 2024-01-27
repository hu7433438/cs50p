#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/17 1:48
# @Author  : QingYang H.
# @File    : faces.py
def convert(a):
    return a.replace(':)', '🙂').replace(':(', '🙁')


def main():
    print('Welcome!\nWriting some sentences containing :), :( or both.')
    print(convert(input()))


main()
