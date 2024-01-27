#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/1/7 15:01
# @Author  : QingYang H.
# @File    : bank.py
def main():
    print(value(input('Greeting:').strip()))


def value(greeting):
    if greeting.startswith('hello'):
        return '$0'
    elif greeting.startswith('h'):
        return '$20'
    else:
        return '$100'


if __name__ == "__main__":
    main()
