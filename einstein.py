#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/17 20:26
# @Author  : QingYang H.
# @File    : einstein.py
def einstein(a):
    return a * 300000000 * 300000000


def main():
    print('Welcome!\nWriting mass as an integer (in kilograms).')
    print(einstein(int(input())))


main()
