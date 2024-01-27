#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/18 21:08
# @Author  : QingYang H.
# @File    : camel.py
camel = input('camelCase: ').strip()
for letter in camel:
    if letter.isupper():
        print(f'_{letter.lower()}', end='')
    else:
        print(letter, end='')
